
import math
import os
import random
import re
import sys


def viralAdvertising(n):
    sharedPeople = 5
    day = 1
    cumulative = 0
    while (day <= n):
        liked = sharedPeople // 2
        cumulative += liked
        sharedPeople = liked * 3
        day += 1
    return cumulative


if __name__ == '__main__':
    n = int(input())

    result = viralAdvertising(n)

    print(result)
