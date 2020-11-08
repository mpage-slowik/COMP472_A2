from time import time
from random import shuffle
import numpy as np

from file_manipulation import output_solution
from x_puzzle import X_Puzzle
from algorithms.uniform_cost import ucs
from algorithms.greedy_best_first import GBF
from algorithms.helpers.heuristics import get_hamming_distance, get_sum_of_permutation
# test_puzz = x_puzzle([0,1,2,3,4,5,6,7])
# print(test_puzz)
# print(ucs(test_puzz))


def run():
    test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    # test_arr = [6, 3, 4, 7, 1, 2, 5, 0]
    # test_arr = [3, 0, 1, 4, 2, 6, 5, 7]
    # test_arr = [0,1,2,3,4,5,6,7]
    # shuffle(test_arr)
    print(test_arr)
    test_puzz1 = X_Puzzle(test_arr)
    # test_puzz1 = X_Puzzle([1,2,3,4,5,6,0,7])
    start_time = time()
    path, attempted = ucs(test_puzz1)
    end_time = time()
    print(end_time - start_time)
    # output_solution(path, "1_ucs_solution.txt", end_time-start_time)

    # print(path)
    # print(attempted)
# test_x = x_puzzle([1,2,3,4,5,6,0,7])
# test_x.move_right()
# print(test_x)
# test_x.move_down()
# print(test_x)

# test_x.move_up()
# print(test_x)

# test_x.move_right()
# print(test_x)
# test_x.move_right()
# print(test_x)
# test_x.move_right()
# print(test_x)


# test_x.move_left()
# print(test_x)

def run_gbf_h1():
    test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz1 = X_Puzzle(test_arr)
    start_time = time()
    solution, search = GBF(test_puzz1, get_hamming_distance)
    end_time = time()
    print(end_time - start_time)

def run_gbf_h2():
    test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz1 = X_Puzzle(test_arr)
    start_time = time()
    solution, search = GBF(test_puzz1, get_sum_of_permutation)
    end_time = time()
    print(end_time - start_time)

if __name__ == "__main__":
    run()
    run_gbf_h1()
    run_gbf_h2()
