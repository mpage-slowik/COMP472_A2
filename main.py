from time import time
from random import shuffle
import numpy as np
import sys
from file_manipulation import output_search, output_solution, output_nosolution
from x_puzzle import X_Puzzle
from algorithms.uniform_cost import ucs
from algorithms.greedy_best_first import GBF
from algorithms.a_star import a_star, a_star_test_admis_mono
from algorithms.helpers.heuristics import get_hamming_distance, get_sum_of_permutation, get_naive,\
    get_modified_hamming_distance, get_modified_sum_of_permutation


def build_random_puzzles():
    curr_arr = ['0', '1', '2', '3', '4', '5', '6', '7']
    with open("input_puzzle.txt", "w") as f:
        for i in range(0, 50):
            shuffle(curr_arr)
            f.write(str(' '.join(curr_arr)) + '\n')


def run_scaled_up_puzzles():
    scale_up = 7
    val = 8
    w = 4
    h = 2
    while val < 35:
        scale = list(range(0, val))
        shuffle(scale)
        goal = list(range(1, val))
        goal.append(0)
        print(scale)
        print(goal)
        run_gbf_h1_for_scale(scale, val, w, h, goal)
        val += scale_up
        scale_up += 2
        w += 1
        h += 1


def run_gbf_h1_for_scale(current_instance, current_execution, width, height, goal):
    print("Greedy Best First, h(n) => modified hamming distance")
    # test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz = X_Puzzle(current_instance, width=width,
                         height=height, goal_state=[goal])
    start_time = time()
    solution, search = GBF(test_puzz, get_modified_hamming_distance)
    end_time = time()
    if solution == None:
        output_nosolution('./scaled_output/' +
                          str(current_execution)+"_gbfs-h1_solution.txt")
        output_nosolution('./scaled_output/' +
                          str(current_execution)+"_gbfs-h1_search.txt")
    else:
        print(end_time - start_time)
        output_solution(solution, './scaled_output/'+str(current_execution) +
                        "_gbfs-h1_solution.txt", end_time-start_time)
        output_search(search, './scaled_output/' +
                      str(current_execution) + "_gbfs-h1_search.txt")


def run_input_file(filename):
    with(open(filename)) as file:
        current_execution = 0
        for line in file:
            current_instance = [int(x) for x in line.split()]
            run_a_star_h1(current_instance, current_execution)
            run_a_star_h2(current_instance, current_execution)
            run_gbf_h1(current_instance, current_execution)
            run_gbf_h2(current_instance, current_execution)
            # run_ucs(current_instance, current_execution)
            current_execution += 1


def run_ucs(current_instance, current_execution):
    print("Universal Cost Search")
    test_puzz = X_Puzzle(current_instance)
    start_time = time()
    solution, search = ucs(test_puzz)
    end_time = time()
    if solution == None:
        output_nosolution(
            './output/'+str(current_execution)+"_ucs_solution.txt")
        output_nosolution('./output/'+str(current_execution)+"_ucs_search.txt")
    else:
        print(end_time - start_time)
        output_solution(solution, './output/'+str(current_execution) +
                        "_ucs_solution.txt", end_time-start_time)
        output_search(search, './output/' +
                      str(current_execution) + "_ucs_search.txt")


def run_gbf_h1(current_instance, current_execution):
    print("Greedy Best First, h(n) => modified hamming distance")
    test_puzz = X_Puzzle(current_instance)
    start_time = time()
    solution, search = GBF(test_puzz, get_modified_hamming_distance)
    end_time = time()
    if solution == None:
        output_nosolution('./output/'+str(current_execution) +
                          "_gbfs-h1_solution.txt")
        output_nosolution(
            './output/'+str(current_execution)+"_gbfs-h1_search.txt")
    else:
        print(end_time - start_time)
        output_solution(solution, './output/'+str(current_execution) +
                        "_gbfs-h1_solution.txt", end_time-start_time)
        output_search(search, './output/' +
                      str(current_execution) + "_gbfs-h1_search.txt")


def run_gbf_h2(current_instance, current_execution):
    print("Greedy Best First, h(n) => modified sum of permutation")
    # test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz = X_Puzzle(current_instance)
    start_time = time()
    solution, search = GBF(test_puzz, get_modified_sum_of_permutation)
    end_time = time()
    if solution == None:
        output_nosolution('./output/'+str(current_execution) +
                          "_gbfs-h2_solution.txt")
        output_nosolution(
            './output/'+str(current_execution)+"_gbfs-h2_search.txt")
    else:
        print(end_time - start_time)
        output_solution(solution, './output/'+str(current_execution) +
                        "_gbfs-h2_solution.txt", end_time-start_time)
        output_search(search, './output/' +
                      str(current_execution) + "_gbfs-h2_search.txt")


def run_a_star_h1(current_instance, current_execution):
    print("A⋆, h(n) => modified hamming distance")
    # test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz = X_Puzzle(current_instance)
    start_time = time()
    solution, search = a_star(test_puzz, get_modified_hamming_distance)
    # solution, search = a_star_test_admis_mono(test_puzz, get_modified_hamming_distance)
    end_time = time()
    if solution == None:
        output_nosolution('./output/'+str(current_execution) +
                          "_astar-h1_solution.txt")
        output_nosolution('./output/'+str(current_execution) +
                          "_astar-h1_search.txt")
    else:
        print(end_time - start_time)
        output_solution(solution, './output/'+str(current_execution) +
                        "_astar-h1_solution.txt", end_time-start_time)
        output_search(search, './output/' +
                      str(current_execution) + "_astar-h1_search.txt")


def run_a_star_h2(current_instance, current_execution):
    print("A⋆, h(n) => modified sum of permutation")
    # test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz = X_Puzzle(current_instance)
    start_time = time()
    solution, search = a_star(test_puzz, get_modified_sum_of_permutation)
    # solution, search = a_star_test_admis_mono(test_puzz, get_modified_sum_of_permutation)
    end_time = time()
    if solution == None:
        output_nosolution('./output/'+str(current_execution) +
                          "_astar-h2_solution.txt")
        output_nosolution('./output/'+str(current_execution) +
                          "_astar-h2_search.txt")
    else:
        print(end_time - start_time)
        output_solution(solution, './output/'+str(current_execution) +
                        "_astar-h2_solution.txt", end_time-start_time)
        output_search(search, './output/' +
                      str(current_execution) + "_astar-h2_search.txt")


def run_GBF_naive():
    print("Greedy Best First, h(n) => naive")
    test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz = X_Puzzle(test_arr)
    start_time = time()
    solution, search = GBF(test_puzz, get_naive)
    end_time = time()
    print("search: "+str(search))
    print("solution: "+str(solution))
    print("time: "+str(end_time-start_time))


def run_a_star_naive():
    print("A⋆, h(n) => naive")
    test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz = X_Puzzle(test_arr)
    start_time = time()
    solution, search = a_star(test_puzz, get_naive)
    end_time = time()
    print("search: "+str(search))
    print("solution: "+str(solution))
    print("time: "+str(end_time-start_time))


if __name__ == "__main__":
    # run_scaled_up_puzzles()
    # run_ucs([1, 2, 4, 7, 3, 0, 5, 6], 0)
    run_input_file('input_puzzle.txt')
    # run_a_star_h1([1, 2, 4, 7, 3, 0, 5, 6], 0)
    # run_a_star_naive()
    # run_GBF_naive()

    sys.exit(0)
