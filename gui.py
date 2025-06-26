import tkinter as tk
# Create the main game window
window=tk.Tk()
window.title("Tic Tac Toe")
window.geometry("300x300")

currentPlayer='X'
# Function to handle button click
def onClick(row,col):
    button=buttons[row][col]
    if button["text"]=="":
        button["text"]=currentPlayer
        button["state"]="disabled" # Disable after clicking
        winner=checkWinner()
        if winner:
            showResult(f"Player {winner} wins!")
        elif isDraw():
            showResult("It's a draw!")
        else:
            switchPlayer()
def switchPlayer():
    global currentPlayer
    if currentPlayer=='X':
        currentPlayer='O'
    else:
        currentPlayer='X'
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
            return buttons[i][0]["text"]
        #check columns
        if buttons[0][i]["text"]==buttons[1][i]["text"]==buttons[2][i]["text"] and buttons[0][i]["text"]!="":
            return buttons[0][i]["text"]
    #check diagonals
    if buttons[0][0]["text"]==buttons[1][1]["text"]==buttons[2][2]["text"] and buttons[0][0]["text"]!="":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"]==buttons[1][1]["text"]==buttons[2][0]["text"] and buttons[0][2]["text"]!="":
        return buttons[0][2]["text"]
    return None
def isDraw():
    for rows in buttons:
        for btn in rows:
            if btn["text"]=="":
                return False
    return True

def showResult(message):
    resultLabel.config(text=message)
    for row in buttons:
        for btn in row:
            btn["state"]="disabled"

resultLabel=tk.Label(window,text="",font=("Arial",16))
resultLabel.grid(row=3,column=0,columnspan=3)
window.mainloop()

