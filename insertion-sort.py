#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for i in range(n):
        j = i - 1;
        while(i != 0 and arr[i] < arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            for a in arr:
                print(a, end=" ")
            print()
            arr[j] = temp
            j += -1
            i += -1
    for a in arr:
        print(a, end=" ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
