#!/bin/python3

import math
import os
import random
import re
import sys
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

if __name__ == '__main__':
    N = int(input())
    if N % 2 != 0:
        print("Weird")
    elif 5>=N>=2 & N %2 == 0:
        print("Not Weird")
    elif 20>=N>=6 & N %2 == 0:
        print("Weird")
    elif N>20 & N %2 == 0:
        print("Not Weird")
