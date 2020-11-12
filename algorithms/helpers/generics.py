
from x_puzzle import Move


def custom_insort(a, x, lo=0, hi=None, key=lambda v: v):
    """ modified insort_right from bisect lib, to accept a key
    """
    x_key = key(x)
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x_key < key(a[mid]):
            hi = mid
        else:
            lo = mid+1
    a.insert(lo, x)


def possible_moves(current_node: Move):
    moves = []
    current_state, up, down, left, right, diag_adj, diag_opp, wrap, wrap_col = current_node.instance.get_instance(), current_node.instance.get_instance(
    ), current_node.instance.get_instance(), current_node.instance.get_instance(), current_node.instance.get_instance(), current_node.instance.get_instance(), current_node.instance.get_instance(), current_node.instance.get_instance(), current_node.instance.get_instance()
    
    if up.move_up():
        moves.append(Move(up, current_node, 'up', current_node.depth +
                          1, 1, up.puzzle[current_state.puzzle.index(0)]))
    if down.move_down():
        moves.append(Move(down, current_node, 'down', current_node.depth +
                          1, 1, down.puzzle[current_state.puzzle.index(0)]))
    if left.move_left():
        moves.append(Move(left, current_node, 'left', current_node.depth +
                          1, 1, left.puzzle[current_state.puzzle.index(0)]))
    if right.move_right():
        moves.append(Move(right, current_node, 'right', current_node.depth +
                          1, 1, right.puzzle[current_state.puzzle.index(0)]))
    if diag_opp.move_opposed_diagonal():
        moves.append(Move(diag_opp, current_node, 'diagonal', current_node.depth +
                          1, 2, diag_opp.puzzle[current_state.puzzle.index(0)]))
    if diag_adj.move_adjacent_diagonal():
        moves.append(Move(diag_adj, current_node, 'diagonal', current_node.depth +
                          1, 2, diag_adj.puzzle[current_state.puzzle.index(0)]))
    if wrap.move_wrap():
        moves.append(Move(wrap, current_node, 'wrap', current_node.depth +
                          1, 3, wrap.puzzle[current_state.puzzle.index(0)]))
    if wrap_col.height > 2:
        if wrap_col.move_wrap_col():
                moves.append(Move(wrap_col, current_node, 'wrap', current_node.depth +
                            1, 3, wrap_col.puzzle[current_state.puzzle.index(0)]))
    return moves
