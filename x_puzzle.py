
class X_Puzzle():

    def __init__(self, puzzle, h=0, g=0, width=4, height=2,goal_state = [[1,2,3,4,5,6,7,0], [1,3,5,7,2,4,6,0]]):
        self.width = width
        self.height = height
        self.h = h
        self.g = g
        self.puzzle = []
        for i in puzzle:
            self.puzzle.append(i)
        self.goal_state = goal_state

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
        if current_loc == -1 or current_loc in list(range(0,self.width)):
            return False
        else:
            move_index = current_loc - self.width
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True

    def move_left(self):
        # [0 if node.value == 0 else -1 for node in self.puzzle].index(0)
        current_loc = self.puzzle.index(0)
        if current_loc == -1 or current_loc%self.width == 0:
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
        if current_loc == -1 or (current_loc + 1)%self.width == 0:
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
        if current_loc == -1 or current_loc in list(range(len(self.puzzle)-self.width, len(self.puzzle))):
            return False
        else:
            move_index = current_loc + self.width
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True

    def move_wrap_col(self):
        current_loc = self.puzzle.index(0)
        bottom_row = list(range(0,self.width))
        top_row  =list(range(len(self.puzzle)-self.width, len(self.puzzle)))
        if current_loc == -1 or (current_loc not in top_row and current_loc not in bottom_row):
            return False
        else:
            move_index = current_loc % self.width if current_loc in top_row else (self.height - 1 ) * self.width + current_loc 
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True

    def move_wrap(self):
        current_loc = self.puzzle.index(0)
        if current_loc == -1 or (current_loc%self.width != 0 and (current_loc + 1)%self.width != 0):
            return False
        else:
            move_index = current_loc + (self.width-1) if current_loc%self.width == 0 else current_loc - (self.width-1)
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True
    
    def move_opposed_diagonal(self):
        top_left_corner = 0
        top_right_corner = self.width-1
        bottom_left_corner = (self.height-1)*self.width
        bottom_right_corner = (self.width*self.height)-1
        current_loc = self.puzzle.index(0)
        if current_loc == -1 or current_loc not in [top_left_corner,top_right_corner,bottom_left_corner, bottom_right_corner]:
            return False
        else:
            if current_loc == top_left_corner:
                move_index = bottom_right_corner
            elif current_loc == top_right_corner:
                move_index = bottom_left_corner
            elif current_loc == bottom_left_corner:
                move_index = top_right_corner
            else:
                move_index = top_left_corner
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True

    def move_adjacent_diagonal(self):
        top_left_corner = 0
        top_right_corner = self.width-1
        bottom_left_corner = (self.height-1)*self.width
        bottom_right_corner = (self.width*self.height)-1
        current_loc = self.puzzle.index(0)
        if current_loc == -1 or current_loc not in [top_left_corner,top_right_corner,bottom_left_corner, bottom_right_corner]:
            return False
        else:
            if current_loc == top_left_corner:
                move_index = self.width+1
            elif current_loc == top_right_corner:
                move_index = top_right_corner*2
            elif current_loc == bottom_left_corner:
                move_index = bottom_left_corner-(self.width-1)
            else:
                move_index = bottom_right_corner-(self.width+1)
            temp = self.puzzle[move_index]
            self.puzzle[move_index] = self.puzzle[current_loc]
            self.puzzle[current_loc] = temp
            return True

    def get_instance(self):
        puzzle = []
        for node in self.puzzle:
            puzzle.append(node)
        return X_Puzzle(puzzle, self.h, self.g, self.width, self.height, self.goal_state)

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
