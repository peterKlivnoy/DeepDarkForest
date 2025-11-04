
import Board_Module

class Piece:

    def __init__(self, starting_x: int, starting_y: int, white: bool):
        self.x = starting_x
        self.y = starting_y
        self.white = white

    
    def get_squares(self):
        pass

    def move(self, x, y):
        pass
    def __str__(self):
         return f"{self.x}, {self.y}, {1 if self.white else 0}"



class Pawn(Piece):
    
    def __init__(self, starting_x, starting_y, white):
        super().__init__(starting_x, starting_y, white)


    def get_squares(self, current_board: 'Board_Module.Board') -> list:
        result = []
        board = current_board.get_state()
        
        if self.white:
            #Attack diagonally right
            if self.x < 7 and board[self.x + 1][self.y + 1] != None:
                    result.append((self.x + 1, self.y + 1))
            
            #Attack diagonally left
            if self.x >0 and board[self.x - 1][self.y + 1] != None:
                    result.append((self.x - 1, self.y + 1))
            
            #Go forward two steps
            if self.y == 1:
                if board[self.x][self.y + 1] == None:
                    result.append((self.x, self.y + 1))
                    if board[self.x][self.y + 2] == None:
                        result.append((self.x, self.y + 2))
            
            #Go forward only one step
            else:
                if board[self.x][self.y + 1] == None:
                    result.append((self.x, self.y + 1))

        else:
             #Attack diagonally right
            if self.x < 7 and board[self.x + 1][self.y - 1] != None:
                    result.append((self.x + 1, self.y - 1))
            
            #Attack diagonally left
            if self.x >0 and board[self.x - 1][self.y - 1] != None:
                    result.append((self.x - 1, self.y - 1))
            
            #Go forward two steps
            if self.y == 7:
                if board[self.x][self.y - 1] == None:
                    result.append((self.x, self.y - 1))
                    if board[self.x][self.y - 2] == None:
                        result.append((self.x, self.y - 2))
            
            #Go forward only one step
            else:
                if board[self.x][self.y - 1] == None:
                    result.append((self.x, self.y - 1))
        
        return result

    def __str__(self):
         return super().__str__()
                 