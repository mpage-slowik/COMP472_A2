from algorithms.helpers.generics import possible_moves
from x_puzzle import X_Puzzle, Move

def ucs(puzzle:X_Puzzle):
    start = Move(puzzle.get_instance(),None,None,0,0,0)
    open_list = []
    closed_list = set()
    pathing = []
    attempted_moves = []
    open_list.append(start)
    current = open_list.pop(0)
    while current.instance.puzzle != puzzle.get_goal():

        # print(closed_list)
        for move in possible_moves(current):
            # move.depth += current.depth
            if move.instance not in closed_list:
                # print(move)
                open_list.append(move)
        open_list.sort(key= lambda x: x.depth)
        attempted_moves.append(current)
        closed_list.add(current.instance)
        if len(open_list) > 0:
            current = open_list.pop(0)
        else:
            return None, None
        print(current)
        # print(closed_list)
        # print(current)
    # attepmted_moves.append(current)
    while(current.parent != None):
        pathing.insert(0,current)
        current=current.parent
    pathing.insert(0,current)
    return pathing, attempted_moves



