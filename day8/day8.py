#!/usr/bin/env python3
#coding=utf-8
#Created on 08 dec. 2021 - by Daniel González Martínez
#day 8.py

import os, sys

#part 1
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, unique_vals_c, unique_e = f.readlines(), [7, 2, 3, 4], 0
    for index, line in enumerate(lines):
        delimited_vals = line.split('|')
        del_delimited_vals = delimited_vals[1].split(' ')
        for val in del_delimited_vals:
            if len(val.rstrip("\n")) in unique_vals_c:
                unique_e += 1

print(unique_e)

#part 2
data = open(os.path.join(sys.path[0], "input.txt"), "r").read().strip().split("\n")
#format lines so [[[vals], [result_code]], [[vals], [result_code]]]
lines = [[["".join(sorted(z)) for z in y.split()] for y in x.split(" | ")] for x in data]
result_code = 0

#rules:
#2 length == 1
#4 length == 4
#3 length == 7
#7 length == 8
#6 length + all letters from 4 (diferenciate from both 5 and 0) == 9
#6 length + diferent from 9 + all letters from 1 (diferenciate from 6)
#6 length + diferent from 9 + diferent from 0
#5 length + all letters from 1 (diferenciate from 5 and 2)
#5 length + diferent from 3 + all letters from 5 to 9 (diferenciate from 2)
#5 length + diferent from 3 + diferent from 5
for nums, digits in lines:
    n1 = [x for x in nums if len(x) == 2][0]
    n4 = [x for x in nums if len(x) == 4][0]
    n7 = [x for x in nums if len(x) == 3][0]
    n8 = [x for x in nums if len(x) == 7][0]
    n9 = [x for x in nums if len(x) == 6 and all(y in x for y in n4)][0]
    n0 = [x for x in nums if len(x) == 6 and x != n9 and all(y in x for y in n1)][0]
    n6 = [x for x in nums if len(x) == 6 and x != n9 and x != n0][0]
    n3 = [x for x in nums if len(x) == 5 and all(y in x for y in n1)][0]
    n5 = [x for x in nums if len(x) == 5 and x != n3 and all(y in n9 for y in x)][0]
    n2 = [x for x in nums if len(x) == 5 and x != n3 and x != n5][0]
    nums = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]

    result_code += int("".join([str(nums.index(x)) for x in digits]))
print(result_code)