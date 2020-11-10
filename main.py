from time import time
from random import shuffle
import numpy as np
import sys
from file_manipulation import output_search, output_solution, output_nosolution
from x_puzzle import X_Puzzle
from algorithms.uniform_cost import ucs
from algorithms.greedy_best_first import GBF
from algorithms.a_star import a_star
from algorithms.helpers.heuristics import get_hamming_distance, get_sum_of_permutation

def build_random_puzzles():
    curr_arr = ['0','1','2','3','4','5','6','7']
    with open("input_puzzle.txt", "w") as f:
        for i in range(0,50):
            shuffle(curr_arr)
            f.write(str(' '.join(curr_arr)) + '\n')

def run_input_file(filename):
    with(open(filename)) as file:
        current_execution = 0
        for line in file:
            current_instance = [int(x) for x in line.split()]
            run_a_star_h1(current_instance,current_execution)
            run_a_star_h2(current_instance,current_execution) 
            run_gbf_h1(current_instance,current_execution)
            run_gbf_h2(current_instance,current_execution)
            run_ucs(current_instance,current_execution)
            current_execution += 1

def run_ucs(current_instance, current_execution):
    print("Universal Cost Search")
    # test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    # test_arr = [6, 3, 4, 7, 1, 2, 5, 0]
    # test_arr = [3, 0, 1, 4, 2, 6, 5, 7]
    # test_arr = [0,1,2,3,4,5,6,7]
    # test_arr = [1,0,3,7,5,2,6,4]
    # shuffle(test_arr)
    # print(current_instance)
    test_puzz = X_Puzzle(current_instance)
    start_time = time()
    solution, search = ucs(test_puzz)
    end_time = time()
    if solution == None:
        output_nosolution('./output/'+str(current_execution)+"_ucs_solution.txt")
        output_nosolution('./output/'+str(current_execution)+"_ucs_search.txt")
    else:
        print(end_time - start_time)
        output_solution(solution, './output/'+str(current_execution)+ "_ucs_solution.txt", end_time-start_time)
        output_search(search,'./output/'+str(current_execution)+ "_ucs_search.txt" )


def run_gbf_h1(current_instance, current_execution):
    print("Greedy Best First, h(n) => hamming distance")
    test_puzz = X_Puzzle(current_instance)
    start_time = time()
    solution, search = GBF(test_puzz, get_hamming_distance)
    end_time = time()
    if solution == None:
        output_nosolution('./output/'+str(current_execution)+"_gbfs-h1_solution.txt")
        output_nosolution('./output/'+str(current_execution)+"_gbfs-h1_search.txt")
    else:
        print(end_time - start_time)
        output_solution(solution, './output/'+str(current_execution)+ "_gbfs-h1_solution.txt", end_time-start_time)
        output_search(search,'./output/'+str(current_execution)+ "_gbfs-h1_search.txt" )


def run_gbf_h2(current_instance, current_execution):
    print("Greedy Best First, h(n) => sum of permutation")
    # test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz = X_Puzzle(current_instance)
    start_time = time()
    solution, search = GBF(test_puzz, get_sum_of_permutation)
    end_time = time()
    if solution == None:
        output_nosolution('./output/'+str(current_execution)+"_gbfs-h2_solution.txt")
        output_nosolution('./output/'+str(current_execution)+"_gbfs-h2_search.txt")
    else:
        print(end_time - start_time)
        output_solution(solution, './output/'+str(current_execution)+ "_gbfs-h2_solution.txt", end_time-start_time)
        output_search(search,'./output/'+str(current_execution)+ "_gbfs-h2_search.txt" )

def run_a_star_h1(current_instance, current_execution):
    print("A⋆, h(n) => hamming distance")
    # test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz = X_Puzzle(current_instance)
    start_time = time()
    solution, search = a_star(test_puzz, get_hamming_distance)
    end_time = time()
    if solution == None:
        output_nosolution('./output/'+str(current_execution)+"_astar-h1_solution.txt")
        output_nosolution('./output/'+str(current_execution)+"_astar-h1_search.txt")
    else:
        print(end_time - start_time)
        output_solution(solution, './output/'+str(current_execution)+ "_astar-h1_solution.txt", end_time-start_time)
        output_search(search,'./output/'+str(current_execution)+ "_astar-h1_search.txt" )

def run_a_star_h2(current_instance, current_execution):
    print("A⋆, h(n) => sum of permutation")
    # test_arr = [1, 0, 3, 6, 5, 2, 7, 4]
    test_puzz = X_Puzzle(current_instance)
    start_time = time()
    solution, search = a_star(test_puzz, get_sum_of_permutation)
    end_time = time()
    if solution == None:
        output_nosolution('./output/'+str(current_execution)+"_astar-h2_solution.txt")
        output_nosolution('./output/'+str(current_execution)+"_astar-h2_search.txt")
    else:
        print(end_time - start_time)
        output_solution(solution, './output/'+str(current_execution)+ "_astar-h2_solution.txt", end_time-start_time)
        output_search(search,'./output/'+str(current_execution)+ "_astar-h2_search.txt" )

if __name__ == "__main__":
    # run_ucs([1, 2, 4, 7, 3, 0, 5, 6], 0)
    run_input_file('input_puzzle.txt')
    # run_ucs()
    # run_gbf_h1()
    # run_gbf_h2()
    # run_a_star_h1()
    # run_a_star_h2()
    sys.exit(0)
