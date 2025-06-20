import random
def getRandomeMove(board):
    availableMoves=[]
    for i in range(9):
        if board[i]==' ':
            availableMoves.append(i)
    if availableMoves:
        return random.choice(availableMoves)
    return None