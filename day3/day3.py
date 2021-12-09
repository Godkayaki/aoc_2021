#!/usr/bin/env python3
#coding=utf-8
#Created on 03 dec. 2021 - by Daniel González Martínez
#day 3.py

#i'll be late on this i know

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

#print(g*e)

#part 2
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, gamma, epsilon, most_c_list, less_c_list = f.readlines(), "", "", [], []
    for index_l, line_vals in enumerate(lines):
        most_c_list.append(line_vals.rstrip("\n"))
        less_c_list.append(line_vals.rstrip("\n"))
    
    for index, line in enumerate(lines[0].rstrip("\n")):
        vals = []
        for index_lines, line_lines in enumerate(lines):
            vals.append(line_lines[index])
        
        try:
            mc, lc = [], []
            for a, b in enumerate(most_c_list):
                mc.append(b[index])
            for a, b in enumerate(less_c_list):
                lc.append(b[index])
            most_common, less_common = max(set(mc), key = mc.count), min(set(lc), key = lc.count)
        
        except: most_common, less_common = max(set(vals), key = vals.count), min(set(vals), key = vals.count)

        zeros, ones = 0, 0
        for val in vals:
            if val == '0': zeros+=1
            elif val == '1': ones+=1

        print("mc: " + str(most_common) + " lc: " + str(less_common))
        print("zeros: " + str(zeros) + " ones:" + str(ones))

        i=0
        for i, line_lines_r in enumerate(lines):
            linea_tww = line_lines_r.rstrip("\n")
            if linea_tww[index] == most_common: 
                try:
                    if len(less_c_list) == 2:
                        for i_t, el in enumerate(less_c_list):
                            if el[index] == '1':
                                less_c_list.remove(el)
                    elif len(less_c_list) != 1: 
                        less_c_list.remove(linea_tww)
                except: pass
            elif linea_tww[index] == less_common:
                try:
                    if len(most_c_list) == 2:
                        for i_t, el in enumerate(most_c_list):
                            if el[index] == '0':
                                most_c_list.remove(el)
                    elif len(most_c_list) != 1: 
                        most_c_list.remove(linea_tww)
                except: pass
            i+=1
    ogr, csr = int(most_c_list[0], 2), int(less_c_list[0], 2)
print(most_c_list[0], less_c_list[0])
print(ogr*csr)