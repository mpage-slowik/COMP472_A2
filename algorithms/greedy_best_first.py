from algorithms.helpers.generics import custom_insort, possible_moves
from x_puzzle import X_Puzzle, Move

def GBF(puzzle:X_Puzzle, heuristic):
    start = Move(puzzle.get_instance(),None,None,0,0,0)
    open_list = []
    closed_list = set()
    pathing = []
    attempted_moves = []
    open_list.append(start)
    current = open_list.pop(0)
    while current.instance.puzzle not in puzzle.get_goal():
        for move in possible_moves(current):
            if move.instance not in closed_list:
                move.h = heuristic(puzzle=move.instance)
                custom_insort(a=open_list, x=move, key=lambda x: x.h)
        attempted_moves.append(current)
        closed_list.add(current.instance)
        if len(open_list) > 0:
            current = open_list.pop(0)
        else:
            return None, None

    while(current.parent != None):
        pathing.insert(0,current)
        current=current.parent
    pathing.insert(0,current)
    return pathing, attempted_moves