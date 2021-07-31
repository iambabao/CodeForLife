# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/3/28
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/3/28
"""


def tokenize(seq):
    return seq.strip().split()


class Trie:
    def __init__(self):
        self.seqs = []

        self.nodes = [[]]
        self.next_index = [{}]

    def add_seqs(self, seqs):
        for seq in seqs:
            if seq in self.seqs:
                continue

            tokens = tokenize(seq)
            seq_id = len(self.seqs)
            self.seqs.append(seq)

            index = 0
            for token in tokens:
                if token not in self.next_index[index]:
                    self.next_index[index][token] = len(self.nodes)
                    self.nodes.append([])
                    self.next_index.append({})
                index = self.next_index[token]
            self.nodes[index].append(seq_id)

    def match(self, seq):
        def _push(index, match):
            if (index, match) not in visited:
                queue.append((index, match))
                visited.append((index, match))

        queue_head = 0
        queue = [(0, 0)]
        visited = []
        matched_results = []

        tokens = tokenize(seq)
        while queue_head < len(queue):
            cur_index, cur_match = queue[queue_head]
            queue_head += 1

            if cur_match == len(tokens):
                for seq_id in self.nodes[cur_index]:
                    matched_results.append(self.seqs[seq_id])
            if cur_match > len(tokens):
                continue
            for next_token, next_index in self.next_index[cur_index].items():
                if next_token == tokens[cur_match]:
                    _push(next_index, cur_match + 1)

        return matched_results
