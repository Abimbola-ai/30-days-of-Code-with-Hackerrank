#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n >= 2:
        for i in range(1,11):
            multiply = n*i
            print(str(n) + " x " + str(i) + " = " + str(multiply))
        
