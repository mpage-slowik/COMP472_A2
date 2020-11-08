# module for puzzle
# can only move 0 with another position


# class Node():
#     def __init__(self, value, cost):
#         self.cost = cost
#         self.value = value
#     def get_value(self):
#         return self.value
#     def get_cost(self):
#         return self.cost
#     def __str__(self):
#         return str(self.get_value())
#     def __repr__(self):
#         return str(self)
#     def __getitem__(self):
#         return self.value
#     def __index__(self):
#         return self.value

class X_Puzzle():
    def __init__(self, puzzle, h=0, g=0):
        self.h = h
        self.g = g
        self.puzzle = []
        for i in puzzle:
            self.puzzle.append(i)
        self.goal_state = list(range(1, len(puzzle)))
        self.goal_state.append(0)

    def __str__(self):
        return str(" ".join(str(i) for i in self.puzzle))

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(tuple(self.puzzle))

    def __eq__(self, other):
        if isinstance(other, X_Puzzle):
            return self.puzzle == other.puzzle
        return False

    def move_up(self):
        # [0 if node.value == 0 else -1 for node in self.puzzle].index(0)
        current_loc = self.puzzle.index(0)
        if current_loc in [-1, 0, 1, 2, 3]:
            return False
        else:
            move_index = current_loc - 4
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True

    def move_left(self):
        # [0 if node.value == 0 else -1 for node in self.puzzle].index(0)
        current_loc = self.puzzle.index(0)
        if current_loc in [-1, 0, 4]:
            return False
        else:
            move_index = current_loc - 1
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True

    def move_right(self):
        # [0 if node.value == 0 else -1 for node in self.puzzle].index(0)
        current_loc = self.puzzle.index(0)
        if current_loc in [-1, 3, 7]:
            return False
        else:
            move_index = current_loc + 1
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True

    def move_down(self):
        # [0 if node.value == 0 else -1 for node in self.puzzle].index(0)
        current_loc = self.puzzle.index(0)
        if current_loc in [-1, 4, 5, 6, 7]:
            return False
        else:
            move_index = current_loc + 4
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True

    def get_instance(self):
        puzzle = []
        for node in self.puzzle:
            puzzle.append(node)
        return X_Puzzle(puzzle)

    def get_goal(self):
        return self.goal_state


class Move:
    def __init__(self, instance: X_Puzzle, parent, move, depth, cost, moved_value):
        self.instance = instance
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.moved_value = moved_value
        self.h = 0
        self.g = 0

    def __hash__(self):
        return hash(tuple(self.instance))

    def __str__(self):
        return '{current:'+str(self.instance)+',  move: ' + str(self.move) + ', depth: ' + str(self.depth) + ', moved_value: ' + str(self.moved_value) + '}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.instance == other.instance
        return False
