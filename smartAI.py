import math
def getBestMove(board,aiSymbol,humanSymbol):
    bestScore=math.inf     # AI tries to minimize human utility
    bestMove=None

    for i in range(9):
        if board[i]==' ':
            board[i]=aiSymbol
            score=miniMax(board,0,True,aiSymbol,humanSymbol)   # Human moves next
            board[i]=' '
            if score<bestScore:
                bestScore=score
                bestMove=i
    return bestMove

def miniMax(board,depth, isHUmanTurn, aiSymbol, humanSymbol):
    winner=checkWinner(board)
    if winner==humanSymbol:
        return 1
    elif winner==aiSymbol:
        return -1
    elif isDraw(board):
        return 0
    
    if isHUmanTurn:
        maxScore=-math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]=humanSymbol
                score=miniMax(board,depth+1,False,aiSymbol,humanSymbol)
                board[i]=' '
                maxScore=max(maxScore,score)
        return maxScore
    else:
        minScore=math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]=aiSymbol
                score=miniMax(board,depth+1,True,aiSymbol,humanSymbol)
                board[i]=' '
                minScore=min(minScore,score)
        return minScore
    
def checkWinner(board):
    winCombinations=[
            [0,1,2],[3,4,5],[6,7,8], #rows
            [0,3,6],[1,4,7],[2,5,8], #columns
            [0,4,8],[2,4,6]          #diagonals
        ]
    for combo in winCombinations:
        a,b,c=combo
        if board[a]==board[b]==board[c] and board[a]!=' ':
            return board[a]
    return None
def isDraw(board):
    return ' ' not in board