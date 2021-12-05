#!/usr/bin/env python3
#coding=utf-8
#Created on 05 dec. 2021 - by Daniel González Martínez
#day 5.py

from collections import Counter
import os, sys, math

board = Counter()

#get diagram
base_diagram = []
for n1 in range(0, 999):
    row = []
    for n2 in range(0,999): row.append(",")
    base_diagram.append(row)

#pass x, y coordinates of the diagam and substitute accordingly
def change_diagram(x, y):
    if base_diagram[y][x] == ",":
        base_diagram[y][x] = "."
    elif base_diagram[y][x] == ".":
        base_diagram[y][x] = 1
    else:
        base_diagram[y][x] = base_diagram[y][x] + 1

#check coords updater
def check_coords_update(x1, y1, x2, y2):
    if x1 > x2: 
        bigger_x = x1
        smaller_x = x2
    else: 
        bigger_x = x2
        smaller_x = x1

    if y1 > y2: 
        bigger_y = y1
        smaller_y = y2
    else: 
        bigger_y = y2
        smaller_y = y1

    for x in range(smaller_x, bigger_x+1):
        for y in range(smaller_y, bigger_y+1):
            #change_diagram(x, y)
            board.update([x, y])

#part1
'''with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, all_values = f.readlines(), []
    for index, line in enumerate(lines):
        vars_line = line.split("->")
        start = list(map(int, vars_line[0].split(",")))
        end = list(map(int, vars_line[1].split(",")))
        check_coords_update(start[0], start[1], end[0], end[1])'''

#at_least_two = len([key for key, value in board.items() if value >=2])
#print(at_least_two)

'''res = 0
for row in base_diagram:
    for value in row:
        if value != "," and value != ".":
            if value >= 2:
                res = res+1

print(res)'''

#part1
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, all_values = f.readlines(), []
    for index, line in enumerate(lines):
        vars_line = line.split("->")
        start = list(map(int, vars_line[0].split(",")))
        end = list(map(int, vars_line[1].split(",")))
        
        #check_coords_update(start[0], start[1], end[0], end[1])
        x1 = start[0]
        y1 = start[1]
        x2 = end[0]
        y2 = end[1]

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for xval in range(int(x2-x1) + 1):
            x = xval
            if y2 > y1:
                for yval in range(int(y2-y1) + 1):
                    y = yval
                    change_diagram(x, y)

res = 0
for row in base_diagram:
    for value in row:
        if value != "," and value != ".":
            if value >= 2:
                res = res+1

print(res)