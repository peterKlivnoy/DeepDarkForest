import Piece 

class Board:

    def __init__(self, n):
        self.dim = n

        self.state = []

        for i in range(n):
            self.state.append([])
            for j in range(n):
                if i == 1:
                    self.state[-1].append(Piece.Pawn(j,i, True))    
                elif i == 7: 
                    self.state[-1].append(Piece.Pawn(j,i, False))
                else:
                     self.state[-1].append(None)




    def get_state(self):
        return self.state.copy()


    def __str__(self):
        return self.get_state()




def __name__():

    Board1 = Board(8)

    print(Board1.get_state())
        