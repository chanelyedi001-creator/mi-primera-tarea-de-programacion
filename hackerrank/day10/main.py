#!/bin/python3

import math
import os
import random
import re
import sys




   

def main():
   
    n = int(input().strip())
    
    
    binary_str = bin(n)[2:]
    
    
    ones_groups = binary_str.split('0')
    
   
    max_consecutive_ones = max(len(group) for group in ones_groups)
    
   
    print(max_consecutive_ones)

if __name__ == '__main__':
    main()
