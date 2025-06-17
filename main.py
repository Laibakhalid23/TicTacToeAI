class TicTacToe:
    def __init__(self):
        self.board=[' ' for _ in range(9)]
    def display(self):
        for i in range(3):
            print('|'.join(self.board[i*3:(i+1)*3]))
            if i<2:
              print('-'*5)
game= TicTacToe()
game.display()