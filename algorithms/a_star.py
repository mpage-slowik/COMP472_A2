from algorithms.helpers.generics import custom_insort, possible_moves
from x_puzzle import X_Puzzle, Move
import copy

def a_star(puzzle:X_Puzzle, heuristic):
    start = Move(puzzle.get_instance(),None,None,0,0,0)
    open_list = []
    closed_list = set()
    pathing = []
    attempted_moves = []
    open_list.append(start)
    current = open_list.pop(0)
    ismonotonic = True
    root = True
    # monotonic test
    # h_root = heuristic(puzzle=current.instance)
    # g_root = current.cost
    while current.instance.puzzle not in puzzle.get_goal():
        for move in possible_moves(current):
            if move.instance not in closed_list:
                move.h = heuristic(puzzle=move.instance)
                move.g = move.parent.g + move.cost
                custom_insort(a=open_list, x=move, key=lambda x: x.h + x.g)
        attempted_moves.append(current)
        closed_list.add(current.instance)
        
        # monotonic test
        # if root:
        #     root = False
        # else:
        #     if (h_root-current.h > current.g-g_root):
        #         ismonotonic = False
        
        if len(open_list) > 0:
            current = open_list.pop(0)
        else:
            return None, None
    actuall_cost = copy.copy(current.g)
    isadmissible = True
    while(current.parent != None):
        if current.h > actuall_cost - current.g:
            isadmissible = False
        pathing.insert(0,current)
        current=current.parent
    pathing.insert(0,current)
    print("admissible: "+ str(isadmissible))
    # print("Monotonic: "+ str(ismonotonic))
    return pathing, attempted_moves