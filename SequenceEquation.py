#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the permutationEquation function below.


def permutationEquation(p):
    pin = deque(p)
    pin.appendleft(0)
    answer = []
    p1 = 0
    p2 = 0
    for i in range(1, len(pin)):
        p1 = pin.index(i)
        p2 = pin.index(p1)
        answer.append(p2)

    return answer


if __name__ == '__main__':

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print(result)
