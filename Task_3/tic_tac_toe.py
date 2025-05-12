import random

print("Welcome to Tic Tac Toe")
print("----------------------")

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows, cols = 3, 3

def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], end=" |")
    print("\n+---+---+---+")

def modifyArray(num, turn):
    row = (num - 1) // 3
    col = (num - 1) % 3
    gameBoard[row][col] = turn

def checkForWinner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            print(f"{board[i][0]} has won!")
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            print(f"{board[0][i]} has won!")
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        print(f"{board[0][0]} has won!")
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        print(f"{board[0][2]} has won!")
        return board[0][2]

    return "N"  # No winner yet

leaveLoop = False
turnCounter = 0

while not leaveLoop:
    printGameBoard()

    if turnCounter % 2 == 0:
        # Player's turn
        try:
            numberPicked = int(input("\nChoose a number [1-9]: "))
            if 1 <= numberPicked <= 9 and numberPicked in possibleNumbers:
                modifyArray(numberPicked, 'X')
                possibleNumbers.remove(numberPicked)
                turnCounter += 1
            else:
                print("Invalid or already chosen number. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
    else:
        # CPU's turn
        cpuChoice = random.choice(possibleNumbers)
        print(f"\nCPU chooses: {cpuChoice}")
        modifyArray(cpuChoice, 'O')
        possibleNumbers.remove(cpuChoice)
        turnCounter += 1

    winner = checkForWinner(gameBoard)
    if winner != "N":
        printGameBoard()
        print("\nGame over! Thank you for playing :)")
        break

    if turnCounter == 9:
        printGameBoard()
        print("\nIt's a draw!")
        break
