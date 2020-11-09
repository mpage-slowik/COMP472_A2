
class X_Puzzle():

    def __init__(self, puzzle, h=0, g=0):
        self.h = h
        self.g = g
        self.puzzle = []
        for i in puzzle:
            self.puzzle.append(i)
        self.goal_state = [[1,2,3,4,5,6,7,0], [1,3,5,7,2,4,6,0]]
        # self.goal_state = list(range(1, len(puzzle)))
        # self.goal_state.append(0)

    def __str__(self):
        return str(" ".join(str(i) for i in self.puzzle))

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(tuple(self.puzzle))

    def __eq__(self, other):
        if isinstance(other, X_Puzzle):
            for i in range(0,len(self.puzzle)):
                if self.puzzle[i] != other.puzzle[i]:
                    return False
            return True
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

    def move_wrap(self):
        current_loc = self.puzzle.index(0)
        if current_loc not in [0, 3, 4, 7]:
            return False
        else:
            move_index = current_loc + 3 if current_loc in [0, 4] else current_loc - 3
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True
    
    def move_opposed_diagonal(self):
        current_loc = self.puzzle.index(0)
        if current_loc not in [0, 3, 4, 7]:
            return False
        else:
            if current_loc == 0:
                move_index = 7
            elif current_loc == 3:
                move_index = 4
            elif current_loc == 4:
                move_index = 3
            else:
                move_index = 0
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True

    def move_adjacent_diagonal(self):
        current_loc = self.puzzle.index(0)
        if current_loc not in [0, 3, 4, 7]:
            return False
        else:
            if current_loc == 0:
                move_index = 5
            elif current_loc == 3:
                move_index = 6
            elif current_loc == 4:
                move_index = 1
            else:
                move_index = 2
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
        return '{current:'+str(self.instance)+',  move: ' + str(self.move) + ', cost: '+str(self.cost) +', depth: ' + str(self.depth) + ', moved_value: ' + str(self.moved_value) + '}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Move):          
            return (self.instance == other.instance )
        return False
