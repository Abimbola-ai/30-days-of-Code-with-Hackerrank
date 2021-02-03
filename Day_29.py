#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    T = int(input().strip())
    for _ in range(T):
        n, k = map(int, input().split())
    
        l = []
        w = []
        for i in range(k - 2, n):
            for j in range(i + 1, n + 1):
                if i < j:
                    bit = i & j
                    if bit < k:
                        l.append(bit)
        m = max(l) 
        print(m)
            
# didn't pass test case 2         
        