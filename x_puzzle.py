#module for puzzle
#can only move 0 with another position


class x_puzzle():
    def __init__(self, top_row = [],bottom_row = []):
        self.top_row = top_row
        self.bottom_row = bottom_row
        self._goal_state = [[1,2,3,4],[5,6,7,0]]

    
    def __str__(self):
        return '['+str(self.top_row) +',' +str(self.bottom_row)+']'
    def __repr__(self):
        return str(self)
    def move_up(self):
        if 0 in self.top_row:
            return False
        else:
            move_index = self.bottom_row.index(0)
            temp = self.top_row[move_index]
            self.top_row[move_index] = 0
            self.bottom_row[move_index] = temp
            return True
    
    def move_left(self):
        if 0 in self.top_row:
            if self.top_row.index(0) == 0:
                return False
            else:
                move_index = (self.top_row.index(0) -1)
                temp = self.top_row[move_index]
                self.top_row[move_index] = 0
                self.top_row[move_index+1] = temp
                return True
        
        elif 0 in self.bottom_row:
            if self.bottom_row.index(0) == 0:
                return False
            else:
                move_index = (self.bottom_row.index(0) - 1)
                temp = self.bottom_row[move_index]
                self.bottom_row[move_index] = 0
                self.bottom_row[move_index+1] = temp
                return True

    def move_right(self):
        if 0 in self.top_row:
            if self.top_row.index(0) == 3:
                return False
            else:
                move_index = (self.top_row.index(0) + 1)
                temp = self.top_row[move_index]
                self.top_row[move_index] = 0
                self.top_row[move_index-1] = temp
                return True
        
        elif 0 in self.bottom_row:
            if self.bottom_row.index(0) == 3:
                return False
            else:
                move_index = (self.bottom_row.index(0) + 1)
                temp = self.bottom_row[move_index]
                self.bottom_row[move_index] = 0
                self.bottom_row[move_index-1] = temp
                return True
    
    def move_down(self):
        if 0 in self.bottom_row:
            return False
        else:
            move_index = self.top_row.index(0)
            temp = self.bottom_row[move_index]
            self.bottom_row[move_index] = 0
            self.top_row[move_index] = temp
            return True

    def get_puzzle(self):
        t_row = []
        b_row = []
        for i in self.top_row:
            t_row.append(i)
        for i in self.bottom_row:
            b_row.append(i)
        return [t_row, b_row]
        
    def get_goal(self):
        return self._goal_state