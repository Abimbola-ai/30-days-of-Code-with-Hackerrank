#!/bin/python3

import math
import os
import random
import re
import sys


def binarynumbers(n):
    binary ="{0:b}".format(n)  # a built-in binary library in python
    print(max(map(len,binary.split("0"))))
    
    
    
if __name__ == '__main__':
    n = int(input())
    binarynumbers(n)
    