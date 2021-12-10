#!/usr/bin/env python3
#coding=utf-8
#Created on 03 dec. 2021 - by Daniel González Martínez
#day 3.py

#i was going crazy with part 2 because i was trying to do both 0 and 1
#at the same time so i borrowed r/Quietuus answer on day3 and i deconstruct
#it to understand it, everything fine, I'm just a fucking idiot ~

import os, sys, copy

#part1
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, gamma, epsilon = f.readlines(), "", ""
    for index, line in enumerate(lines[0].rstrip("\n")):
        zeros, ones = 0, 0
        for index_lines, line_lines in enumerate(lines):
            if line_lines[index] != "\n":
                if int(line_lines[index]) == 0: zeros = zeros + 1
                elif int(line_lines[index]) == 1: ones = ones + 1 
        if zeros > ones: 
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        elif ones > zeros: 
            gamma = gamma + "1"
            epsilon = epsilon + "0"
    g, e = int(gamma, 2), int(epsilon, 2)

print(g*e)

#part 2
def bit_counter(array, index):
    zeroes, ones = 0, 0
    for line in array:
        if line[index] == "0":
            zeroes += 1
        if line[index] == "1":
            ones += 1
    return zeroes, ones
    
def most(zeroes, ones):
    if ones >= zeroes:
        return '1'
    else:
        return '0'

def least(zeroes, ones):
    if ones >= zeroes:
        return '0'
    else:
        return '1'
 
def recursive_search(array, index, mode):
    if len(array) == 1:
        return array[0]
    else:
        zeroes, ones = bit_counter(array, index)
        if mode == 'most':
            current_column = most(zeroes, ones)
        elif mode == 'least':
            current_column = least(zeroes, ones)
        new_array = []
        for item in array:
            if item[index] == current_column:
                new_array.append(item)
        index += 1
        return recursive_search(new_array, index, mode)

string_array = []
with open(os.path.join(sys.path[0], "input.txt"), "r") as in_file:
    for line in in_file:
        string_array.append(line.strip('\n'))       

print(int(recursive_search(string_array,0, 'most'), 2) * int(recursive_search(string_array,0, 'least'), 2))