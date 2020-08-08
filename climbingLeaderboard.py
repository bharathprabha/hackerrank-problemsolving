#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.


def climbingLeaderboard(scores, alice):
    scores_set = list(set(scores))
    scores_set.sort(reverse=True)
    result = []
    l = len(scores_set)
    for s in alice:
        while (l > 0) and (s >= scores_set[l-1]):
            l -= 1
        result.append(l+1)
    return result


if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print(result)
