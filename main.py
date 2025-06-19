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

  
if __name__ == "__main__":  
    game= TicTacToe()
while True:
    game.display()
    game.makeMove()
    game.switchPlayer()         

