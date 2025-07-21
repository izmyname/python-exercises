import random

class TicTacToe:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = self.first_player()
        self.is_playing = True
        
    # create a board for the game   
    def create_board(self):
        board = []
        for i in range(3):
            board.append(["_"]*3)
            
        return board
    
    # create a board to display to the players
    def display_board(self):
        return f"\n| {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} | \n-------------\n| {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |\n-------------\n| {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} | \n-------------\n"
    
    # choose random player for the first move
    def first_player(self):
        player=""
        if random.randint(0,1) == 0:
            player="X"
        else:
            player="O"
        return player
    
    # make a move
    def move(self, board, row, col, player):
        if 0<=col<3 and 0<=row<3 and board[row][col] == "_":
            board[row][col]= player
        else:
            raise ValueError
            
    # pass the turn to the next player
    def swap_player(self):
        if self.current_player == "X":
                self.current_player = "O"
        else:
            self.current_player = "X"
        return self.current_player
    
    # end game if there's a winner
    def end_game(self, player):
        print(self.display_board())
        print(f"player {player} won!")
        self.is_playing=False
    
    # define the winner
    def is_winner(self, board, player):
        # check rows
        for row in board:
            if row[0]==row[1]==row[2]==player:
                self.end_game(player)
        # check columns
        for i in range(3):
            if board[0][i]==board[1][i]==board[2][i]==player:
                self.end_game(player)
        #check diagonals
        if board[0][0]==board[1][1]==board[2][2]==player or board[2][0]==board[1][1]==board[0][2]==player:
            self.end_game(player)
        # check if the board filled
        if "_" not in board[0] and "_" not in board[1] and "_" not in board[2]:
            print(self.display_board())
            print("It's a draw!")
            self.is_playing=False

            

    
    def start(self):
        while self.is_playing:
            print(self.display_board())
            print(f"Player {self.current_player} move")
            try:
                row = int(input("Choose the row. 0-2: "))
                col = int(input("Choose the column. 0-2: "))
                self.move(self.board,row, col,self.current_player)
            except ValueError:
                print("\nInvalid input. Try again")
            else:
                self.is_winner(self.board,self.current_player)
                self.swap_player()

    

tic_tac_toe = TicTacToe()
tic_tac_toe.start()