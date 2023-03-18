import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
Winner = None
gameRunning = True

# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


# take player input
def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("Ooops the spot is already taken. Please take another spot!!!")

# Check for win or tie
def checkHorizontle(board):
    global Winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        Winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        Winner = board[6]
        return True

def checkVerical(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        Winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        Winner = board[2]
        return True
    
def checkDiag(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        Winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        Winner = board[3]
        return True
    
def CheckIfTie(baord):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie !!!!")
        gameRunning = False

def checkIFWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {Winner} !!!")
        gameRunning = False
    elif checkVerical(board):
        printBoard(board)
        print(f"The winner is {Winner} !!!")
        gameRunning = False
    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {Winner} !!!")
        gameRunning = False


# Switch Player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIFWin(board)
    CheckIfTie(board)
    switchPlayer()
    computer(board)
    checkIFWin(board)
    CheckIfTie(board)