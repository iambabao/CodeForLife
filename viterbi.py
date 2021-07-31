# -*- coding:utf-8  -*-

"""
@Author             : Bao
@Date               : 2021/3/27
@Desc               :
@Last modified by   : Bao
@Last modified date : 2021/3/27
"""


def viterbi(obs, trans, emit, pi):
    """

    :param obs: (num_steps,)
    :param trans: (num_states, num_states)
    :param emit: (num_states, num_obs)
    :param pi: (num_states,)
    :return:
    """

    dp = [[0] * len(obs) for _ in range(len(pi))]  # (num_states, num_steps)
    path = [[-1] * len(obs) for _ in range(len(pi))]  # (num_states, num_steps)

    for i in range(len(pi)):
        dp[i][0] = pi[i] * emit[i][obs[0]]

    for step in range(1, len(obs)):
        for i in range(len(pi)):
            for j in range(len(pi)):
                score = dp[j][step-1] * trans[j][i] * emit[i][obs[step]]
                if score > dp[i][step]:
                    dp[i][step] = score
                    path[i][step] = j

    answer = dp[0][-1]
    last_state = 0
    for i in range(1, len(pi)):
        if dp[i][-1] > answer:
            answer = dp[i][-1]
            last_state = i

    answer_path = [last_state]
    for step in range(len(obs) - 1, 0, -1):
        last_state = path[last_state][step]
        answer_path.append(last_state)

    return answer, answer_path[::-1]
