#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(arr):
    result = []      #Store result in a list
    for i in range(0,4):    # row section of the array
        for j in range(0,4): # column section of the array
            sum_of_hourglass = sum(arr[i][j:j+3])+ arr[i+1][j+1] + sum(arr[i+2][j:j+3]) # 1 hourglass equation
            result.append(sum_of_hourglass) # append sum_of hourglass to result list
    print(max(result)) #print maximum value in the list

    

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hourglass(arr)
