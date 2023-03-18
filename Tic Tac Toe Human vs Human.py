board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player1 = 'O'
player2 = 'X'

# game board
def printBoard(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("\n")


# check for position
def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


# displaying the winner 
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Its a draw!!!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("player1 wins!!!")
                exit()
            else:
                print("player2 wins!!!")
                exit()
        return
    else:
        print("Invalid position!!!")
        position = int(input("Please enter new position 1-9:  "))
        insertLetter(letter, position)
        return


#check for win or draw
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


# player switching and player input
def player1Move():
    position = int(input("Enter the position for 'O' 1-9:  "))
    insertLetter(player1, position)
    return

def player2Move():
    position = int(input("Enter the position for 'X' 1-9:  "))
    insertLetter(player2, position)
    return

printBoard(board)

while not checkForWin():
    player2Move()
    player1Move()