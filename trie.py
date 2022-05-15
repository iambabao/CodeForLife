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
    def __init__(self, seqs=None):
        self.nodes = [[]]  # stores the matched sequences
        self.next_index = [{}]  # stores the index of next node

        if seqs is not None:
            for seq in seqs:
                self.insert_seq(seq)

    def insert_seq(self, seq):
        tokens = tokenize(seq)

        index = 0
        for token in tokens:
            if token not in self.next_index[index]:
                self.next_index[index][token] = len(self.nodes)
                self.nodes.append([])
                self.next_index.append({})
            index = self.next_index[index][token]
        self.nodes[index].append(seq)  # TODO: de-duplication

    def delete_seq(self, seq):
        tokens = tokenize(seq)

        cur_index, cur_match = 0, 0
        while cur_match < len(tokens):
            cur_token = tokens[cur_match]
            if cur_token not in self.next_index[cur_index]:
                return
            cur_index, cur_match = self.next_index[cur_index][cur_token], cur_match + 1
        self.nodes[cur_index] = []

    def exact_match(self, seq):
        tokens = tokenize(seq)

        cur_index, cur_match = 0, 0
        while cur_match < len(tokens):
            cur_token = tokens[cur_match]
            if cur_token not in self.next_index[cur_index]:
                return None
            cur_index, cur_match = self.next_index[cur_index][cur_token], cur_match + 1

        return self.nodes[cur_index][0] if len(self.nodes[cur_index]) > 0 else None

    def prefix_match(self, seq):
        tokens = tokenize(seq)

        cur_index, cur_match = 0, 0
        while cur_match < len(tokens):
            cur_token = tokens[cur_match]
            if cur_token not in self.next_index[cur_index]:
                return []
            cur_index, cur_match = self.next_index[cur_index][cur_token], cur_match + 1

        queue = [cur_index]
        queue_head = 0
        matched_results = []
        while queue_head < len(queue):
            cur_index = queue[queue_head]
            queue_head += 1
            matched_results.extend(self.nodes[cur_index])
            for next_index in self.next_index[cur_index].values():
                queue.append(next_index)

        return matched_results


def main():
    sequences = [
        'import numpy',
        'import numpy as np',
        'import numpy as xx',
        'from collections import defaultdict',
    ]

    trie = Trie(sequences)

    results = trie.exact_match('import numpy')
    print(results)
    results = trie.prefix_match('import numpy')
    print(results)


if __name__ == '__main__':
    main()
