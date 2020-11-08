
def get_hamming_distance(puzzle):
    hamming_distance = 0
    for pos in range(len(puzzle.puzzle)):
        if puzzle.puzzle[pos] != puzzle.goal_state[pos]:
            hamming_distance = hamming_distance + 1
    return hamming_distance

def get_sum_of_permutation(puzzle):
    sum_of_permutation = 0
    for index, element in enumerate(puzzle.puzzle[:-1]):
        goal_index = puzzle.goal_state.index(element) 
        goal_left_side = puzzle.goal_state[:goal_index]
        for right_element in puzzle.puzzle[index+1:]:
            if right_element in goal_left_side:
                sum_of_permutation = sum_of_permutation+1
    return sum_of_permutation

