from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1 , text="Tic Tac Toe" , font=("Arial" , 30) , bg="orange" )
titleLabel.pack()

frame2 = Frame(root)
frame2.pack()

board = { 1:" " , 2:" " , 3:" ",
          4:" " , 5:" " , 6:" ",
          7:" " , 8:" " , 9:" " }

turn = "x"


def checkForWin(player):
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True


# Function to play
def play(event):
    global turn 
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    print(clicked)
    if clicked == "n" :
        clicked = 1
    else :
        clicked = int(clicked)
    
    if button["text"] == " ":
        if turn == "x" :
            button["text"] = "X"
            board[clicked] = turn
            turn = "o"
            
        else:
            button["text"] = "O"
            board[clicked] = turn
            turn = "x"

    print(board)
    if checkForWin(turn):
        print(turn , "wins the game")
        print("Game over")

        
# Tic Tac Toe Board 

#  First row 

button1 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="yellow" , relief=RAISED , borderwidth=5)
button1.grid(row = 0 , column=0)
button1.bind("<Button-1>" , play)

button2 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button2.grid(row = 0 , column=1)
button2.bind("<Button-1>" , play)

button3 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button3.grid(row = 0 , column=2)
button3.bind("<Button-1>" , play)

#  second row 

button4 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button4.grid(row = 1 , column=0)
button4.bind("<Button-1>" , play)

button5 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button5.grid(row = 1 , column=1)
button5.bind("<Button-1>" , play)

button6 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button6.grid(row = 1 , column=2)
button6.bind("<Button-1>" , play)

#  third row 

button7 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="yellow" , relief=RAISED , borderwidth=5)
button7.grid(row = 2 , column=0)
button7.bind("<Button-1>" , play)

button8 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="yellow" , relief=RAISED , borderwidth=5 )
button8.grid(row = 2 , column=1)
button8.bind("<Button-1>" , play)

button9 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="yellow" , relief=RAISED , borderwidth=5)
button9.grid(row = 2 , column=2)
button9.bind("<Button-1>" , play)



root.mainloop()