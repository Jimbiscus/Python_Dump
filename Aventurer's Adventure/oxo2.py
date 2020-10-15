PLAYER_1 = 'X'
PLAYER_2 = 'O'

board = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]]



# --- Functions ---

def display():
    txt = "  01234\n"
    y = 0
    for row in board:
        txt += str(y) + " "
        y += 1
        for data in row:
            txt += data
        txt += "\n"
    print(txt)

def give(x, y):
    return board[y][x]

def place(carac):
    x = int(input("x : "))
    y = int(input("y : "))
    board[y][x] = carac


def init():
    for n in range(len(board)):
        del board[0]
        board.append(['.', '.', '.', '.', '.'])

def is_full():
    full = True

    for row in board:
        for data in row:
            if data == '.':
                full = False

    return full
def is_xxx():
    for row in board:
        pass
# --- here start the script ---

x = 0
while True:
    if x == 0: 
        print("Player One")
        place(PLAYER_1)
        display()
        x = 1
        is_full()
    elif x == 1:
        
        print("Player Two")
        place(PLAYER_2)
        display()
        x = 0
        is_full()