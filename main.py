import random
class TicTacToe:
    def __init__(self):
        self.board=[' ' for _ in range(9)]
        self.currentPlayer=random.choice(['X','O'])
    def display(self):
        for i in range(3):
            print('|'.join(self.board[i*3:(i+1)*3]))
            if i<2:
              print('-'*5)
    def makeMove(self):
        while True:
            try:
                print(f"Player {self.currentPlayer}'s turn. Enter a position from 1 to 9: ")
                move= int(input( ))-1
                if move<0 or move>8:
                    print("Invalid position. Please enter a number between 1 and 9")
                elif self.board[move]!=' ':
                    print("The position is already taken.")
                else:
                    self.board[move]=self.currentPlayer
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")    
    def switchPlayer(self):
        if self.currentPlayer=='X':
            self.currentPlayer='O'
        else:
            self.currentPlayer='X'
    def checkWinner(self):
        winCombinations=[
            [0,1,2],[3,4,5],[6,7,8], #rows
            [0,3,6],[1,4,7],[2,5,8], #columns
            [0,4,8],[2,4,6]          #diagonals
        ]
        for combo in winCombinations:
            a,b,c=combo
            if self.board[a]==self.board[b]==self.board[c] and self.board[a]!=' ':
                return True
        return False
    def isDraw(self):
        for cell in self.board:
            if cell == ' ':
                return False
        return True
    def aiMove(self):
        print("Computer's turn:")
        availableMoves=[]
        for i in range(9):
            if self.board[i]==' ':
                availableMoves.append(i)
        move=random.choice(availableMoves)
        self.board[move]=self.currentPlayer

if __name__ == "__main__":  
    vsComputer=input("Do you want to play against Computer? (y/n) " ).lower()=='y'
    if vsComputer:
        humanSymbol=input("Choose your symbol (X/O) " ).upper()
        while humanSymbol not in ['X','O']:
            humanSymbol=input("Invalid choice. Please choose X or O: " ).upper()
        if humanSymbol=='X':
            aiSymbol='O'
        else:
            aiSymbol='X'
    else:
        humanSymbol=None  #not needed in player vs player mode
        aiSymbol=None

    game= TicTacToe()
    while True:
        game.display()

        if vsComputer and game.currentPlayer==aiSymbol:
            game.aiMove()
        else:
             game.makeMove()
             
        if game.checkWinner():
            game.display()
            print(f"Player {game.currentPlayer} wins!")
            break
        elif game.isDraw():
            game.display()
            print(f"Its a draw!")
            break
        game.switchPlayer()         

    
