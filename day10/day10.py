#!/usr/bin/env python3
#coding=utf-8
#Created on 10 dec. 2021 - by Daniel González Martínez
#day 10.py

import os, sys, copy

#part 1
lines, res = [] , 0
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    for line in f:
        lines.append(line.rstrip("\n"))

#dictionaries with key-value
type_, value = { "(": ")", "{": "}", "[": "]", "<": ">" }, { ")": 3, "]": 57, "}": 1197, ">": 25137 }

for line in lines:
    st = []
    for index in line:
        if index in type_: st.append(type_[index])
        elif index == st[-1]: st.pop()
        else:
            res += value[index]

print(res)

#part 2
lines, res = [] , 0
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    for line in f:
        lines.append(line.rstrip("\n"))

#dictionaries with key-value
type_, value = { "(": ")", "{": "}", "[": "]", "<": ">" }, { ")": 1, "]": 2, "}": 3, ">": 4 }

okay_lines, scores = [], []
for line in lines:
    st, ok_l = [], True
    for index in line:
        if index in type_: st.append(type_[index])
        elif index == st[-1]: st.pop()
        else:
            ok_l = False
            break
    
    if ok_l != False: okay_lines.append(line)

for line in okay_lines:
    st, single_score = [], 0
    for index in line:
        if index in type_: st.append(type_[index])
        elif index == st[-1]: st.pop()
    
    for el in reversed(st):
        single_score = single_score * 5 + value[el]
    scores.append(single_score)

scores.sort()
print(scores[int((len(scores)/2))])