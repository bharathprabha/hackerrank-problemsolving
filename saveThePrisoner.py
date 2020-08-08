import math
import os
import random
import re
import sys


def saveThePrisoner(n, m, s):
    return(((S - 1 + M - 1) % N) + 1)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(result)
