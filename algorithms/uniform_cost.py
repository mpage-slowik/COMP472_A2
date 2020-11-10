from algorithms.helpers.generics import possible_moves
from x_puzzle import X_Puzzle, Move
from threading import Timer
_universal_exit = False

def exitfunc():
    global _universal_exit
    _universal_exit = True

def ucs(puzzle:X_Puzzle):
    global _universal_exit
    _universal_exit = False
    start = Move(puzzle.get_instance(),None,None,0,0,0)
    open_list = []
    closed_list = set()
    pathing = []
    attempted_moves = []
    open_list.append(start)
    current = open_list.pop(0)
    timer_func = Timer(60, exitfunc) # exit in 60 seconds
    timer_func.start()
    while current.instance.puzzle not in puzzle.get_goal():
        if _universal_exit is True:
            return None,None
        for move in possible_moves(current):
            move.g = move.cost + current.cost
            move.h = 0
            # move.cost += current.cost
            if move.instance not in closed_list:
                if move in open_list:
                    current_index = open_list.index(move)
                    if move.cost < open_list[current_index].cost:
                        open_list[current_index] = move
                else:
                    open_list.append(move)
        open_list.sort(key= lambda x: (x.depth,x.cost))

        attempted_moves.append(current)
        closed_list.add(current.instance)
        if len(open_list) > 0:
            current = open_list.pop(0)
        else:
            return None, None
        # print(current)
    timer_func.cancel()
    while(current.parent != None):
        pathing.insert(0,current)
        current=current.parent
    pathing.insert(0,current)

    return pathing, attempted_moves



