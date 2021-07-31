# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/7/31
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/7/31
"""

import torch


def beam_search(encoder_states, decoder, beam_size, max_length):
    cur_ids = torch.full([beam_size, 1], decoder.sos_id)
    cur_states = torch.zeros([beam_size, decoder.hidden_size], dtype=torch.float)
    cur_log_prob = torch.zeros([beam_size, 1], dtype=torch.float)

    for cur_step in range(max_length - 1):
        # (beam_size, vocab_size), (beam_size, hidden_size)
        output_logits, states = decoder(encoder_states, cur_ids, cur_states)

        # (beam_size, vocab_size)
        log_prob = cur_log_prob + torch.log(torch.softmax(output_logits, dim=-1))

        if cur_step == 0:
            top_k_scores, top_k_ids = torch.topk(log_prob[0], k=beam_size)
        else:
            top_k_scores, top_k_ids = torch.topk(log_prob, k=beam_size)
        beam_ids = top_k_ids // decoder.vocab_size  # (beam_size,)
        token_ids = top_k_ids % decoder.vocab_size  # (beam_size,)

        # update
        cur_ids = torch.cat(cur_ids[beam_ids], token_ids.unsqueeze(-1))
        cur_states = states
        cur_log_prob = log_prob

    return cur_ids, cur_log_prob
