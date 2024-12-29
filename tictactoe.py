def custom_sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    board = [str(i) for i in range(9)]
    for i in range(9):
        if xState[i]:
            board[i] = 'X'
        elif zState[i]:
            board[i] = 'O'
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [2, 5, 8], [1, 4, 7], [0, 3, 6], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if custom_sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X won the match!")
            return 1
        if custom_sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O won the match!")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0] * 9
    zState = [0] * 9
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe!")
    while True:
        printBoard(xState, zState)
        print(f"{'X' if turn == 1 else 'O'}'s Chance")
        try:
            value = int(input("Please enter a value (0-8): "))
            if value < 0 or value > 8 or xState[value] or zState[value]:
                print("Invalid input. Try again.")
                continue
        except ValueError:
            print("Invalid input. Enter a number between 0 and 8.")
            continue
        
        if turn == 1:
            xState[value] = 1
        else:
            zState[value] = 1

        result = checkWin(xState, zState)
        if result != -1:
            printBoard(xState, zState)
            break

        if sum(xState) + sum(zState) == 9:  # Check for a draw
            print("It's a draw!")
            printBoard(xState, zState)
            break

        turn = 1 - turn
