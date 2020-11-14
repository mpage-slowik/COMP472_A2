import sys

def get_naive(puzzle):
    best = sys.maxsize
    for goal in puzzle.goal_state:
        tmp = _get_specific_naive(puzzle.puzzle, goal)
        if best > tmp:
            best = tmp
    return best

def _get_specific_naive(puzzle, goal):
    if puzzle[-1] == 0:
        return 0
    return 1

def get_hamming_distance(puzzle):
    best = sys.maxsize
    for goal in puzzle.goal_state:
        tmp = _get_specific_hamming_distance(puzzle.puzzle, goal)
        if best > tmp:
            best = tmp
    return best

def _get_specific_hamming_distance(puzzle, goal):
    hamming_distance = 0
    for pos in range(len(puzzle)):
        if puzzle[pos] != goal[pos]:
            hamming_distance = hamming_distance + 1
    return hamming_distance

def get_modified_hamming_distance(puzzle):
    best = sys.maxsize
    for goal in puzzle.goal_state:
        tmp = _get_specific_modified_hamming_distance(puzzle.puzzle, goal)
        if best > tmp:
            best = tmp
    return best

def _get_specific_modified_hamming_distance(puzzle, goal):
    hamming_distance = 0
    pos = 0
    while(pos<len(puzzle)):
        if puzzle[pos] != goal[pos]:
            hamming_distance = hamming_distance + 1
        pos += 2
    return hamming_distance

def get_sum_of_permutation(puzzle):
    best = sys.maxsize
    for goal in puzzle.goal_state:
        tmp = _get_specific_sum_permutation(puzzle.puzzle, goal)
        if best > tmp:
            best = tmp
    return best

def get_modified_sum_of_permutation(puzzle):
    best = sys.maxsize
    for goal in puzzle.goal_state:
        tmp = _get_specific_sum_permutation(puzzle.puzzle, goal)
        if best > tmp:
            best = tmp
    return best//6

def _get_specific_sum_permutation(puzzle, goal):
    sum_of_permutation = 0
    for index, element in enumerate(puzzle[:-1]):
        goal_index = goal.index(element) 
        goal_left_side = goal[:goal_index]
        for right_element in puzzle[index+1:]:
            if right_element in goal_left_side:
                sum_of_permutation = sum_of_permutation+1
    return sum_of_permutation

