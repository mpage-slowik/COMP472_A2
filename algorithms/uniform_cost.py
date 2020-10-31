from x_puzzle import x_puzzle

def possible_moves(puzzle:x_puzzle):
    moves = []        
    up, down, left, right = x_puzzle(puzzle.get_puzzle()[0], puzzle.get_puzzle()[1]) , x_puzzle(puzzle.get_puzzle()[0], puzzle.get_puzzle()[1]), x_puzzle(puzzle.get_puzzle()[0], puzzle.get_puzzle()[1]), x_puzzle(puzzle.get_puzzle()[0], puzzle.get_puzzle()[1])
    if up.move_up():
        moves.append(up)
    if down.move_down():
        moves.append(down)
    if left.move_left():
        moves.append(left)
    if right.move_right():
        moves.append(right)
    return moves

def ucs(puzzle:x_puzzle):
    current = x_puzzle(puzzle.get_puzzle()[0], puzzle.get_puzzle()[1])
    fringe = []
    path = []
    fringe.append(current)
    while puzzle.get_puzzle() != puzzle.get_goal():
        for move in possible_moves(current):
            print("test")



