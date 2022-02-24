#!/bin/env python3

import ast
from operator import itemgetter

def main():
    with open('a_an_example.in.txt', 'r') as text:
        nums = [ast.literal_eval(i) for i in text]
        data = [str(i) + '\n' for i in sorted(nums)]

    with open('test.txt', 'w') as text:
        text.writelines(data)

if __name__== "__main__":
    main()