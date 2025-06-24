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


window.mainloop()

