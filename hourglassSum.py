#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    highestsum = float('-inf')
    arSum = 0
    for i in range(0, len(arr[0])-2):
        for j in range(0, len(arr[0])-2):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                arr[i + 1][j + 1] + arr[i + 2][j] + \
                arr[i + 2][j + 1] + arr[i + 2][j + 2]
            highestsum = sum if sum > highestsum else highestsum
    return highestsum


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
