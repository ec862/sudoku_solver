# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:53:54 2020

@author: Edward Carrington
"""

import numpy as np

# Load sudokus
sudokus = np.load("data/sudokus.npy")
print("Shape of one sudoku array:", sudokus[0].shape, ". Type of array values:", sudokus.dtype)

# Load solutions
solutions = np.load("data/sudoku_solutions.npy")
print("Shape of one sudoku solution array:", solutions[0].shape, ". Type of array values:", solutions.dtype, "\n")

def move_possible(x,y,n,sudoku):
        for i in range(0,9):
            if sudoku[y][i] == n or sudoku[i][x] == n:
                return False
        squareX = (x//3)*3
        squareY = (y//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if sudoku[squareY + j][squareX + i] == n:
                    return False
        return True
    
def solve(sudoku):
    for y in range(0,9):
        for x in range(0,9):
            if sudoku[y][x] == 0:
                for i in range(1,10):
                    if move_possible(x,y,i,sudoku):
                        sudoku[y][x] = i
                        if solve(sudoku):
                            return True
                        sudoku[y][x] = 0
                return False
    return True

def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """        
    solved_sudoku = np.copy(sudoku)
    unsolveable = np.full((9, 9), -1, dtype=int)
    
    solve(solved_sudoku)    
    for y in range(0,9):
        for x in range(0,9):
            if solved_sudoku[y][x] == 0:
               return unsolveable

    return solved_sudoku


print(sudokus[1])
print(sudoku_solver(sudokus[1]))
print(solutions[1])
print()