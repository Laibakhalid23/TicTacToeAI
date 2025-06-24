from game import TicTacToe
from randomAI import getRandomeMove
from smartAI import getBestMove

def chooseGameMode():
    print("\nChoose Game Mode:")
    print("1. Human vs Human")
    print("2. Human vs Random AI")
    print("3. Human vs Smart AI")

    while True:
        choice=input("Enter 1,2, or 3: ")
        if choice in ['1','2','3']:
            return int(choice)
        else:
            print("Invalid choice. Please try again.")

def chooseSymbol():
    while True:
        symbol = input("Choose your symbol (X/O): ").upper()
        if symbol in ['X', 'O']:
            return symbol, 'O' if symbol == 'X' else 'X'
        print("Invalid input. Please enter X or O.")

if __name__ == "__main__":
    mode=chooseGameMode()
    game=TicTacToe()
    
    if mode==1:
        print("\n--- Human vs Human ---")
        while True:
            game.display()
            game.makeMove()
            if game.checkWinner():
                game.display()
                print(f" Player {game.currentPlayer} wins!")
                break
            elif game.isDraw():
                game.display()
                print(f"It's a Draw!")
                break
            game.switchPlayer()
    
    else:
        playerSymbol,aiSymbol=chooseSymbol()
        if mode==2:
            aiType="Random AI"
        else:
            aiType="Smart AI"

        print(f"\n--- Human vs {aiType} ---")
        print(f"You are {playerSymbol}. {aiType} is {aiSymbol}.")

        while True:
            game.display()

            if game.currentPlayer== playerSymbol:
                game.makeMove()
            else:
                print(f"{aiType}'s Turn:")
                if mode==2:
                    move=getRandomeMove(game.board)
                else:
                    move=getBestMove(game.board,aiSymbol,playerSymbol)
                game.board[move]=aiSymbol

            if game.checkWinner():
                game.display()
                print(f"Player {game.currentPlayer} wins!")
                break
            elif game.isDraw():
                game.display()
                print("It's a draw!")
                break

            game.switchPlayer()



