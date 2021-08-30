class game:
    def __init__(self):
        self.player = 1
        self.board = []
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(' ')

    def get_open_spots(self):
        open_spots = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    open_spots.append((i, j))

        return open_spots
                    
    def is_valid_move(self, r, c):
        if (r, c) in self.get_open_spots():
            return True
        else:
            return False
        
    def make_move(self):
        r = int(input("Row: "))
        c = int(input("Column: "))
                
        if self.is_valid_move(r, c):
            self.board[r][c] = self.player
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1

        else:
            print("\nINVALID MOVE\n")
                
    def check_for_winner(self):
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]

        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        for i in range(3):
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]

            if self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
            
        if len(self.get_open_spots()) == 0:
            return 0

        else:
            return -1
     

g = game()
print("\n\tTIC-TAC-TOE\n")
for i in range(3):
    for j in range(3):
        print(g.board[i][j], end = '')
        if j != 2:
            print("|", end = '')
    print()
    
while True:
    print("\nTurn -- Player:", g.player)
    g.make_move()
    print()
    for i in range(3):
        for j in range(3):
            print(g.board[i][j], end = '')
            if j != 2:
                print("|", end = '')
        print()

    if g.check_for_winner() == 0:
        print("\nGame Drawn. No moves remaining.")
        break
    
    if g.check_for_winner() == 1 or g.check_for_winner() == 2:
        print("\nPlayer", g.check_for_winner(), "WINS!!!")
        print()
        break
    

