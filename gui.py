import tkinter as tk
import tkinter.simpledialog as simpledialog
import random
from smartAI import getBestMove


# Create the main game window
window=tk.Tk()
window.title("Tic Tac Toe")
window.state("zoomed")  # Make window full screen
window.configure(bg="#d4e6f1")  # Soft blue background
window.withdraw()  # Hide window temporarily

# Ask for game mode
gameMode = simpledialog.askstring("Game Mode", "Choose mode:\n1. Human vs Human\n2. Human vs Random AI\n3. Human vs Smart AI")

if gameMode not in ["1", "2", "3"]:
    gameMode = "1"  # Default to Human vs Human if invalid input

window.deiconify()  # Show main window after dialog
currentPlayer='X'
usedCells = [[False for _ in range(3)] for _ in range(3)]
# Function to handle button click
def onClick(row,col):
    if usedCells[row][col]:
        return  # Ignore if already used
    button=buttons[row][col]
    if button["text"]=="":
        button["fg"] = "blue" if currentPlayer == "X" else "red"
        usedCells[row][col] = True
        button["text"]=currentPlayer
        winner,winCells=checkWinner()
        if winner:
            highlightWinningLine(winCells)
            showResult(f"Player {winner} wins!")
        elif isDraw():
            showResult("It's a draw!")
        else:
            switchPlayer()
            if gameMode in ["2","3"] and currentPlayer=="O":
                window.after(500,aiMove) # Delay for better UX

def switchPlayer():
    global currentPlayer
    if currentPlayer=='X':
        currentPlayer='O'
    else:
        currentPlayer='X'

def aiMove():
    if gameMode=="2":
        emptyCells=[]
        for r in range(3):
            for c in range(3):
                if not usedCells[r][c]:
                    emptyCells.append((r,c))
        if not emptyCells:
            return
        row,col=random.choice(emptyCells)
    elif gameMode=="3":
         # Convert GUI 2D board to flat list of 9 cells
         flatBoard=[]
         for r in range(3):
             for c in range(3):
                 val=buttons[r][c]["text"]
                 flatBoard.append(val if val!="" else " ")

         #calling smartAI function
         move=getBestMove(flatBoard,"O","X")
         if move is None:
             return
         # Convert 1D move index back to 2D row, col
         row = move // 3
         col = move % 3

    onClick(row,col)

# Create a 3x3 grid of buttons
buttons=[]
for row in range(3):
    rowButtons=[]
    for col in range(3):
        btn=tk.Button(window,text="",font=('Arial',24),width=5,height=2,command= lambda r=row, c=col:onClick(r,c))
        btn.grid(row=row,column=col)
        rowButtons.append(btn)
    buttons.append(rowButtons)

def checkWinner():
    for i in range(3):
        #check rows
        if buttons[i][0]["text"]==buttons[i][1]["text"]==buttons[i][2]["text"] and buttons[i][0]["text"]!="":
            return buttons[i][0]["text"],[(i,0),(i,1),(i,2)]
        #check columns
        if buttons[0][i]["text"]==buttons[1][i]["text"]==buttons[2][i]["text"] and buttons[0][i]["text"]!="":
            return buttons[0][i]["text"], [(0, i), (1, i), (2, i)]
    #check diagonals
    if buttons[0][0]["text"]==buttons[1][1]["text"]==buttons[2][2]["text"] and buttons[0][0]["text"]!="":
        return buttons[0][0]["text"], [(0, 0), (1, 1), (2, 2)]
    if buttons[0][2]["text"]==buttons[1][1]["text"]==buttons[2][0]["text"] and buttons[0][2]["text"]!="":
        return buttons[0][2]["text"], [(0, 2), (1, 1), (2, 0)]
    return None,[]

def isDraw():
    for rows in buttons:
        for btn in rows:
            if btn["text"]=="":
                return False
    return True

def showResult(message):
    resultLabel.config(text=message)
    for r in range(3):
        for c in range(3):
            usedCells[r][c] = True 
            buttons[r][c]["state"] = "disabled"
resultLabel=tk.Label(window,text="",font=("Arial",16),bg="#d4e6f1")
resultLabel.grid(row=3,column=0,columnspan=3)


def resetGame():
    global currentPlayer
    currentPlayer = 'X'
    resultLabel.config(text="")
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", fg="black", state="normal", bg="SystemButtonFace")
            usedCells[r][c] = False
resetButton=tk.Button(window, text="Play Again",font=("Arial",12),command=resetGame,bg="#aed6f1")
resetButton.grid(row=4,column=0,columnspan=3,pady=10)

def highlightWinningLine(cells):
    for row, col in cells:
        buttons[row][col].config(bg="#82E0AA")  # Light green highlight


window.mainloop()

