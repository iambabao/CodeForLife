# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/7/31
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/7/31
"""

import torch
import torch.nn as nn


def scaled_dot_product_attention(q, k, v, mask, temperature):
    """

    :param q: (..., seq_length_q, hidden_size)
    :param k: (..., seq_length, hidden_size)
    :param v: (..., seq_length, hidden_size)
    :param mask: (..., seq_length_q, seq_length_k)
    :param temperature:
    :return:
    """
    qk = torch.matmul(q, k.transpose(-1, -2)) / temperature  # (..., seq_length_q, seq_length)
    if mask is not None:
        qk += (mask * -1e9)

    attention_weights = torch.softmax(qk, dim=-1)  # (..., seq_length_q, seq_length)
    output = torch.matmul(attention_weights, v)  # (..., seq_length, hidden_size)

    return output, attention_weights


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model

        assert d_model % self.num_heads == 0

        self.depth = d_model // self.num_heads

        self.wq = nn.Linear(d_model, d_model)
        self.wk = nn.Linear(d_model, d_model)
        self.wv = nn.Linear(d_model, d_model)

        self.dense = nn.Linear(d_model, d_model)

    def split_heads(self, x, batch_size):
        """
        Split the last dimension into (num_heads, depth).
        Transpose the result such that the shape is (batch_size, num_heads, seq_len, depth)
        """
        x = x.view(x, [batch_size, -1, self.num_heads, self.depth])
        return x.transpose(0, 2, 1, 3)

    def forward(self, q, v, k, mask):
        batch_size = q.shape[0]

        q = self.wq(q)  # (batch_size, seq_length_q, d_model)
        k = self.wk(k)  # (batch_size, seq_length, d_model)
        v = self.wv(v)  # (batch_size, seq_length, d_model)

        q = self.split_heads(q, batch_size)  # (batch_size, num_heads, seq_length_q, depth)
        k = self.split_heads(k, batch_size)  # (batch_size, num_heads, seq_length, depth)
        v = self.split_heads(v, batch_size)  # (batch_size, num_heads, seq_length, depth)

        # scaled_attention.shape == (batch_size, num_heads, seq_length_q, depth)
        # attention_weights.shape == (batch_size, num_heads, seq_length_q, seq_length)
        output, attention_weights = scaled_dot_product_attention(q, k, v, mask, temperature=self.depth ** 0.5)

        # (batch_size, seq_length_q, d_model)
        output = output.transpose(1, 2).view([batch_size, -1, self.d_model])

        # (batch_size, seq_length_q, d_model)
        output = self.dense(output)

        return output, attention_weights


class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, dff, rate=0.1):
        super(EncoderLayer, self).__init__()

        self.mha = MultiHeadAttention(d_model, num_heads)

        self.ffn = nn.Sequential(
            nn.Linear(d_model, dff),
            nn.ReLU(),
            nn.Linear(dff, d_model),
        )

        self.layer_norm1 = nn.LayerNorm(d_model, eps=1e-6)
        self.layer_norm2 = nn.LayerNorm(d_model, eps=1e-6)

        self.dropout1 = nn.Dropout(rate)
        self.dropout2 = nn.Dropout(rate)

    def call(self, x, mask):
        attn_output, _ = self.mha(x, x, x, mask)  # (batch_size, seq_length, d_model)
        attn_output = self.dropout1(attn_output)
        out1 = self.layer_norm1(x + attn_output)  # (batch_size, seq_length, d_model)

        ffn_output = self.ffn(out1)  # (batch_size, seq_length, d_model)
        ffn_output = self.dropout2(ffn_output)
        out2 = self.layer_norm2(out1 + ffn_output)  # (batch_size, seq_length, d_model)

        return out2


class DecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, dff, rate=0.1):
        super(DecoderLayer, self).__init__()

        self.mha1 = MultiHeadAttention(d_model, num_heads)
        self.mha2 = MultiHeadAttention(d_model, num_heads)

        self.ffn = nn.Sequential(
            nn.Linear(d_model, dff),
            nn.ReLU(),
            nn.Linear(dff, d_model),
        )

        self.layer_norm1 = nn.LayerNorm(d_model, eps=1e-6)
        self.layer_norm2 = nn.LayerNorm(d_model, eps=1e-6)
        self.layer_norm3 = nn.LayerNorm(d_model, eps=1e-6)

        self.dropout1 = nn.Dropout(rate)
        self.dropout2 = nn.Dropout(rate)
        self.dropout3 = nn.Dropout(rate)

    def call(self, x, enc_output, look_ahead_mask, padding_mask):
        attn1, attn_weights_block1 = self.mha1(x, x, x, look_ahead_mask)
        attn1 = self.dropout1(attn1)
        out1 = self.layer_norm1(attn1 + x)  # (batch_size, seq_length, d_model)

        attn2, attn_weights_block2 = self.mha2(out1, enc_output, enc_output, padding_mask)
        attn2 = self.dropout2(attn2)
        out2 = self.layer_norm2(attn2 + out1)  # (batch_size, seq_length, d_model)

        ffn_output = self.ffn(out2)  # (batch_size, seq_length, d_model)
        ffn_output = self.dropout3(ffn_output)
        out3 = self.layer_norm3(ffn_output + out2)  # (batch_size, seq_length, d_model)

        return out3, attn_weights_block1, attn_weights_block2


class Encoder(nn.Module):
    def __init__(self, num_layers, d_model, num_heads, dff, rate=0.1):
        super(Encoder, self).__init__()

        self.num_layers = num_layers

        self.enc_layers = nn.ModuleList(EncoderLayer(d_model, num_heads, dff, rate) for _ in range(num_layers))

    def call(self, x, mask):
        # (batch_size, seq_length, d_model)
        for layer in self.enc_layers:
            x = layer(x, mask)

        return x


class Decoder(nn.Module):
    def __init__(self, num_layers, d_model, num_heads, dff, rate=0.1):
        super(Decoder, self).__init__()

        self.num_layers = num_layers

        self.dec_layers = nn.ModuleList(DecoderLayer(d_model, num_heads, dff, rate) for _ in range(num_layers))

    def call(self, x, enc_output, look_ahead_mask, padding_mask):
        attention_weights = {}

        for i, layer in self.dec_layers:
            x, block1, block2 = layer(x, enc_output, look_ahead_mask, padding_mask)

            attention_weights['decoder_layer_{}_block_1'.format(i + 1)] = block1
            attention_weights['decoder_layer_{}_block_2'.format(i + 1)] = block2

        return x, attention_weights
