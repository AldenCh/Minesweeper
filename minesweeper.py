from tkinter import *
import random

root = Tk()
root.title("Minesweeper")
root.iconbitmap("mine.ico")

root.withdraw()

launcher = Toplevel()
launcher.title("Minesweeper Launcher")
launcher.iconbitmap("mine.ico")
launcher.geometry("+800+400")

bombs = []

minefield = []

boardframe = LabelFrame(root)
boardframe.grid(row=0, column=0, sticky=N+S+E+W)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

score = 0

class Mine:
    def __init__(self, buttonw, buttonh, posx, posy, val):
        self.width = buttonw
        self.height = buttonh
        self.positionx = posx
        self.positiony = posy
        self.value = val
        self.mbutton = Button(boardframe, width=self.width, height=self.height, bg="purple", command= lambda: clearmine(self.positionx, self.positiony, self.width, self.height))
        self.mbutton.grid(row=posy, column=posx, sticky=N+S+E+W)
    def getButton(self):
        return self.mbutton
    def getValue(self):
        return self.value

# Make the board and close the launcher
def gamestart():
    global bombs
    if (difficulty.get() == "Easy"):
        for i in range(15):
            while(True):
                coord = str(random.randint(0,7)) + "," + str(random.randint(0,7))
                new = True
                for x in range(len(bombs)):
                    if (bombs[x] == coord):
                        new = False
                if (new == True):
                    bombs.append(coord)
                    break
        with open("board.txt", "w") as output_file:
            for i in range(8):
                line = ""
                for j in range(8):
                    match = False
                    for x in range(len(bombs)):
                        coord = str(i) + "," + str(j)
                        if (bombs[x] == coord):
                            match = True
                    if (match == True):
                        line += "X"
                    else:
                        line += "O"
                if (i == 7):
                    output_file.write(line)
                else:
                    output_file.write(line+"\n")
                minefield.append(line)
    elif (difficulty.get() == "Medium"):
        bombs = []
        for i in range(30):
            while(True):
                coord = str(random.randint(0,12)) + "," + str(random.randint(0,12))
                new = True
                for x in range(len(bombs)):
                    if (bombs[x] == coord):
                        new = False
                if (new == True):
                    bombs.append(coord)
                    break
        with open("board.txt", "w") as output_file:
            for i in range(13):
                line = ""
                for j in range(13):
                    match = False
                    for x in range(len(bombs)):
                        coord = str(i) + "," + str(j)
                        if (bombs[x] == coord):
                            match = True
                    if (match == True):
                        line += "X"
                    else:
                        line += "O"
                if (i == 12):
                    output_file.write(line)
                else:
                    output_file.write(line+"\n")
                minefield.append(line)
    elif (difficulty.get() == "Hard"):
        bombs = []
        for i in range(50):
            while(True):
                coord = str(random.randint(0,19)) + "," + str(random.randint(0,19))
                new = True
                for x in range(len(bombs)):
                    if (bombs[x] == coord):
                        new = False
                if (new == True):
                    bombs.append(coord)
                    break
        with open("board.txt", "w") as output_file:
            for i in range(20):
                line = ""
                for j in range(20):
                    match = False
                    for x in range(len(bombs)):
                        coord = str(i) + "," + str(j)
                        if (bombs[x] == coord):
                            match = True
                    if (match == True):
                        line += "X"
                    else:
                        line += "O"
                if (i == 19):
                    output_file.write(line)
                else:
                    output_file.write(line+"\n")
                minefield.append(line)
    minesweeper()

def clearmine(x, y, w, h):
    global root
    global buttonfield
    global score
    if (buttonfield[y][x].getValue() == "X"):
        buttonfield[y][x].getButton().destroy()
        root.withdraw()
        finishWindow = Toplevel()
        posx = 900
        posy = 500
        finishWindow.geometry()
        finishWindow.geometry("+" + str(posx) + "+" + str(posy))
        finishText = Label(finishWindow, text="Nice Try, your final score is "+str(score))
        finishText.pack()
        newButton = Button(finishWindow, text="Game Over", command=root.destroy)
        newButton.pack()
    else:
        max = 0
        if (difficulty.get() == "Easy"):
            max = 7
        elif (difficulty.get() == "Medium"):
            max = 12
        elif (difficulty.get() == "Hard"):
            max = 19
        score += 1
        buttonfield[y][x].getButton().destroy()
        mines = 0
        if (y == 0):
            if (x == 0):
                if (minefield[y][x+1] == "X"):
                    mines += 1
                if (minefield[y+1][x] == "X"):
                    mines += 1
                if (minefield[y+1][x+1] == "X"):
                    mines += 1
            elif (x == max):
                if (minefield[y][x-1] == "X"):
                    mines += 1
                if (minefield[y+1][x] == "X"):
                    mines += 1
                if (minefield[y+1][x-1] == "X"):
                    mines += 1
            else:
                if (minefield[y][x-1] == "X"):
                    mines += 1
                if (minefield[y+1][x] == "X"):
                    mines += 1
                if (minefield[y+1][x-1] == "X"):
                    mines += 1
                if (minefield[y][x+1] == "X"):
                    mines += 1
                if (minefield[y+1][x+1] == "X"):
                    mines += 1
        elif (y == max):
            if (x == 0):
                if (minefield[y][x+1] == "X"):
                    mines += 1
                if (minefield[y-1][x] == "X"):
                    mines += 1
                if (minefield[y-1][x+1] == "X"):
                    mines += 1
            elif (x == max):
                if (minefield[y][x-1] == "X"):
                    mines += 1
                if (minefield[y-1][x] == "X"):
                    mines += 1
                if (minefield[y-1][x-1] == "X"):
                    mines += 1
            else:
                if (minefield[y][x+1] == "X"):
                    mines += 1
                if (minefield[y-1][x] == "X"):
                    mines += 1
                if (minefield[y-1][x+1] == "X"):
                    mines += 1
                if (minefield[y][x-1] == "X"):
                    mines += 1
                if (minefield[y-1][x-1] == "X"):
                    mines += 1
        elif (x == 0):
            if (minefield[y][x+1] == "X"):
                mines += 1
            if (minefield[y-1][x] == "X"):
                mines += 1
            if (minefield[y+1][x] == "X"):
                mines += 1
            if (minefield[y-1][x+1] == "X"):
                mines += 1
            if (minefield[y+1][x+1] == "X"):
                mines += 1
        elif (x == max):
            if (minefield[y][x-1] == "X"):
                mines += 1
            if (minefield[y-1][x] == "X"):
                mines += 1
            if (minefield[y+1][x] == "X"):
                mines += 1
            if (minefield[y-1][x-1] == "X"):
                mines += 1
            if (minefield[y+1][x-1] == "X"):
                mines += 1
        else:
            if (minefield[y][x-1] == "X"):
                mines += 1
            if (minefield[y][x+1] == "X"):
                mines += 1
            if (minefield[y-1][x] == "X"):
                mines += 1
            if (minefield[y+1][x] == "X"):
                mines += 1
            if (minefield[y-1][x-1] == "X"):
                mines += 1
            if (minefield[y-1][x+1] == "X"):
                mines += 1
            if (minefield[y+1][x-1] == "X"):
                mines += 1
            if (minefield[y+1][x+1] == "X"):
                mines += 1
        if (mines == 0):
            newLabel = Label(boardframe, width=w, height=h, relief=SUNKEN)
        else:
            newLabel = Label(boardframe, text=str(mines), width=w, height=h, relief=SUNKEN)
        newLabel.grid(row=y, column=x, sticky=N+S+E+W)
        if (difficulty.get() == "Easy"):
            if (score == 49):
                boardframe.destroy()
                reminder.destroy()
                win = Label(root, text="Nice Job Man Baby Steps!")
                win.grid(row=0, column=0, columnspan=8, rowspan=8)
        elif (difficulty.get() == "Medium"):
            if (score == 139):
                boardframe.destroy()
                reminder.destroy()
                win = Label(root, text="This May Be Medium But It Still Pretty Difficult, Nice Job!")
                win.grid(row=0, column=0, columnspan=13, rowspan=13)
        elif (difficulty.get() == "Hard"):
            if (score == 350):
                boardframe.destroy()
                reminder.destroy()
                win = Label(root, text="You Really Sat There And Cleared All 350 Squares... Congrats But Have You Ever Thought Of Picking Up A Hobby?")
                win.grid(row=0, column=0, columnspan=20, rowspan=20)

prompt = Label(launcher, text="Choose a Difficulty")
prompt.grid(row=0, column=0, ipadx=10, ipady=10, columnspan=3, sticky=W+E+N)

easy = Label(launcher, text="Easy Difficulty\n-8x8 Board\n-15 Bombs", bg="green")
easy.grid(row=1, column=0, ipadx=10, ipady=10, sticky=W+E)
medium = Label(launcher, text="Medium Difficulty\n-13x13 Board\n-30 Bombs", bg="yellow")
medium.grid(row=1, column=1, ipadx=10, ipady=10, sticky=W+E)
hard = Label(launcher, text="Hard Difficulty\n-20x20 Board\n-50 Bombs", bg="red")
hard.grid(row=1, column=2, ipadx=10, ipady=10, sticky=W+E)

difficulties = ["Easy", "Medium", "Hard"]
difficulty = StringVar()
difficulty.set("Easy")
drop = OptionMenu(launcher, difficulty, *difficulties)
drop.grid(row=2, column=0, columnspan=3)

choose = Button(launcher, text="Choose Difficulty", borderwidth=10, command=gamestart)
choose.grid(row=3, column=0, ipadx=10, ipady=10, columnspan=3, sticky=W+E+S)
buttonfield = []

# Run the actual game
def minesweeper():
    global boardframe
    global launcher
    global root
    global buttonfield
    global reminder
    root.deiconify()
    launcher.destroy()
    rows = 0
    cols = 0
    buttonheight = 0
    buttonwidth = 0
    labeltext = ""
    rspan = 0
    cspan = 0
    bgcolour = ""
    if (difficulty.get() == "Easy"):
        root.geometry("472x499+750+200")
        rows = 8
        cols = 8
        rspan = 8
        cspan = 18
        buttonheight = 3
        buttonwidth = 7
        labeltext = "Easy Difficulty\n-8x8 Board\n-15 Bombs"
        bgcolour = "green"
    elif (difficulty.get() == "Medium"):
        root.geometry("708x780+600+100")
        rows = 13
        cols = 13
        rspan = 13
        cspan = 18
        buttonheight = 3
        buttonwidth = 7
        labeltext = "Medium Difficulty\n-13x13 Board\n-30 Bombs"
        bgcolour = "yellow"
    elif (difficulty.get() == "Hard"):
        root.geometry("900x871+525+100")
        rows = 20
        cols = 20
        rspan = 20
        cspan = 18
        buttonheight = 2
        buttonwidth = 5
        labeltext = "Hard Difficulty\n-20x20 Board\n-50 Bombs"
        bgcolour = "red"
    with open("board.txt", "r") as input_file:
        currentx = 0
        currenty = 0
        counter = 0
        for line in input_file:
            currentrow = []
            Grid.rowconfigure(boardframe, counter, weight=1)
            for i in range(cols):
                Grid.columnconfigure(boardframe, i, weight=1)
                if (str(line[i]) == "X"):
                    currentrow.append(Mine(buttonwidth, buttonheight, currentx, currenty, "X"))
                else:
                    currentrow.append(Mine(buttonwidth, buttonheight, currentx, currenty, "O"))
                currentx += 1
            buttonfield.append(currentrow)
            currenty += 1
            currentx = 0
            counter += 1
    reminder = Label(root, text=labeltext, bg=bgcolour, width=cspan)
    reminder.grid(row=rows, column=0, rowspan=rspan, columnspan=rspan, sticky=W+E+N+S)
    
root.mainloop()