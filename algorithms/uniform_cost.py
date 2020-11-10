from algorithms.helpers.generics import possible_moves
from x_puzzle import X_Puzzle, Move
from threading import Timer
_universal_exit = False
def exitfunc():
    _universal_exit = True

def ucs(puzzle:X_Puzzle):
    start = Move(puzzle.get_instance(),None,None,0,0,0)
    open_list = []
    closed_list = set()
    pathing = []
    attempted_moves = []
    open_list.append(start)
    current = open_list.pop(0)
    Timer(60, exitfunc).start() # exit in 60 seconds
    while current.instance.puzzle not in puzzle.get_goal():
        if _universal_exit:
            return None,None
        # print(open_list)
        # print(closed_list)
        for move in possible_moves(current):
            move.cost += current.cost
            if move.instance not in closed_list:
                if move in open_list:
                    current_index = open_list.index(move)
                    if move.cost < open_list[current_index].cost:
                        open_list.remove(open_list[current_index])
                        open_list.append(move)
                else:
                    open_list.append(move)
        open_list.sort(key= lambda x: (x.depth,x.cost))

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



