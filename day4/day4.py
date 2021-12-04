#!/usr/bin/env python3
#coding=utf-8
#Created on 04 dec. 2021 - by Daniel González Martínez
#day 4.py

import os, sys, copy

#check board
def check_board(board):
    for row in board:
        if row.count("x") == 5:
            return True

    for index, value in enumerate(board[0]):
        if board[0][index] == "x" and board[1][index] == "x" and board[2][index] == "x" and board[3][index] == "x" and board[4][index] == "x":
            return True

#part1
def part1():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        lines, all_boards, board = f.readlines(), [], []
        for index, line in enumerate(lines):
            if index == 0: nums_int = list(map(int, line.split(",")))
            else:
                if line == "\n" and index != 1:
                    all_boards.append(board)
                    board = []
                else:
                    new_row_int = list(map(int, line.split()))
                    if len(new_row_int) != 0: board.append(new_row_int)

        for num in nums_int:
            for index_board, board in enumerate(all_boards):
                for index_row, row in enumerate(board):
                    for index_ele, element in enumerate(row):
                        if element == num:
                            all_boards[index_board][index_row][index_ele] = "x"

                if not check_board(board): pass
                else:
                    sum_ = 0
                    for row in board:
                        for element in row:
                            if element != "x": 
                                sum_ = sum_ + element
                    return sum_*num
print(part1())

#part2
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, all_boards, board, boards_completion = f.readlines(), [], [], []
    for index, line in enumerate(lines):
        if index == 0: nums_int = list(map(int, line.split(",")))
        else:
            if line == "\n" and index != 1:
                all_boards.append(board)
                board = []
            else:
                new_row_int = list(map(int, line.split()))
                if len(new_row_int) != 0: board.append(new_row_int)

    for num in nums_int:
        for index_board, board in enumerate(all_boards):
            for index_row, row in enumerate(board):
                for index_ele, element in enumerate(row):
                    if element == num:
                        all_boards[index_board][index_row][index_ele] = "x"

            if not check_board(board): pass
            else:
                if all_boards.index(board) not in boards_completion:
                    boards_completion.append(all_boards.index(board))
                    if len(boards_completion) == len(all_boards):
                        last_num = num
                        last_board_check = copy.deepcopy(board)

last_board, sum_ = boards_completion[-1:][0], 0
for row in last_board_check:
    for element in row:
        if element != "x": 
            sum_ = sum_ + element
print(last_num*sum_)