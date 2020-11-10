from time import time
from random import shuffle
import numpy as np

from file_manipulation import output_solution
from x_puzzle import X_Puzzle
from algorithms.uniform_cost import ucs
from algorithms.greedy_best_first import GBF
from algorithms.a_star import a_star
from algorithms.helpers.heuristics import get_hamming_distance, get_sum_of_permutation
from threading import Timer


def run_ucs():
    test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    # test_arr = [6, 3, 4, 7, 1, 2, 5, 0]
    # test_arr = [3, 0, 1, 4, 2, 6, 5, 7]
    # test_arr = [0,1,2,3,4,5,6,7]
    test_arr = [1,0,3,7,5,2,6,4]
    # shuffle(test_arr)
    print(test_arr)
    test_puzz1 = X_Puzzle(test_arr)
    start_time = time()


    path, attempted = ucs(test_puzz1)
    if path == None:
        print("no solution")
    end_time = time()
    print(end_time - start_time)

    print(len(path))
    # output_solution(path, "1_ucs_solution.txt", end_time-start_time)

    # print(path)
    # print(attempted)


def run_gbf_h1():
    print("Greedy Best First, h(n) => hamming distance")
    test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz1 = X_Puzzle(test_arr)
    start_time = time()
    solution, search = GBF(test_puzz1, get_hamming_distance)
    end_time = time()
    print("time: "+str(end_time - start_time))
    print(len(solution))

def run_gbf_h2():
    print("Greedy Best First, h(n) => sum of permutation")
    test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz1 = X_Puzzle(test_arr)
    start_time = time()
    solution, search = GBF(test_puzz1, get_sum_of_permutation)
    end_time = time()
    print("time: "+str(end_time - start_time))
    print(len(solution))

def run_a_star_h1():
    print("A⋆, h(n) => hamming distance")
    test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz1 = X_Puzzle(test_arr)
    start_time = time()
    solution, search = a_star(test_puzz1, get_hamming_distance)
    end_time = time()
    print("time: "+str(end_time - start_time))
    print(len(solution))

def run_a_star_h2():
    print("A⋆, h(n) => sum of permutation")
    test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz1 = X_Puzzle(test_arr)
    start_time = time()
    solution, search = a_star(test_puzz1, get_sum_of_permutation)
    end_time = time()
    print("time: "+str(end_time - start_time))
    print(len(solution))

if __name__ == "__main__":
    run_ucs()
    run_gbf_h1()
    run_gbf_h2()
    run_a_star_h1()
    run_a_star_h2()
