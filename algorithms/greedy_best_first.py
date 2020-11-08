from x_puzzle import X_Puzzle, Move
from algorithms.heuristics import get_hamming_distance, get_sum_of_permutation

def possible_moves(current_node:Move):
    moves = []
    current_state, up, down, left, right = current_node.instance.get_instance(), current_node.instance.get_instance(), current_node.instance.get_instance(), current_node.instance.get_instance(), current_node.instance.get_instance()
    if up.move_up():
        moves.append(Move(up,current_node,'up',current_node.depth + 1, 1, up.puzzle[current_state.puzzle.index(0)]))
    if down.move_down():
        moves.append(Move(down,current_node,'down',current_node.depth + 1, 1, down.puzzle[current_state.puzzle.index(0)]))
    if left.move_left():
        moves.append(Move(left,current_node,'left',current_node.depth + 1, 1, left.puzzle[current_state.puzzle.index(0)]))
    if right.move_right():
        moves.append(Move(right,current_node,'right',current_node.depth + 1, 1, right.puzzle[current_state.puzzle.index(0)]))
    return moves

def GBF(puzzle:X_Puzzle):
    start = Move(puzzle.get_instance(),None,None,0,0,0)
    open_list = []
    closed_list = set()
    pathing = []
    attempted_moves = []
    open_list.append(start)
    current = open_list.pop(0)
    print(puzzle)
    print(puzzle.goal_state)
    print('')
    print(get_sum_of_permutation(puzzle))

def GBF_r(puzzle:X_Puzzle):
    start = Move(puzzle.get_instance(),None,None,0,0,0)
    open_list = []
    closed_list = set()
    pathing = []
    attempted_moves = []
    open_list.append(start)
    current = open_list.pop(0)
    while current.instance.puzzle != puzzle.get_goal():
        for move in possible_moves(current):
            if move.instance not in closed_list:
    
                open_list.append(move)
        open_list.sort(key= lambda x: x.depth)
        attempted_moves.append(current)
        closed_list.add(current.instance)
        if len(open_list) > 0:
            current = open_list.pop(0)
        else:
            return None, None
        print(current)

    while(current.parent != None):
        pathing.insert(0,current)
        current=current.parent
    pathing.insert(0,current)
    return pathing, attempted_moves