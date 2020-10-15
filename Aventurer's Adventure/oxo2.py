PLAYER_1 = 'X'
PLAYER_2 = 'O'

board = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]]



# --- Functions ---
# display the board and its indexes
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
# returns what's at the x y position of the board
def give(x, y):
    return board[y][x]
# place stuff on board
def place(carac, x, y):
    board[y][x] = carac
# resets the board
def init():
    for n in range(len(board)):
        del board[0]
        board.append(['.', '.', '.', '.', '.'])
# checks if the board has no "."
def is_full():
    full = True

    for row in board:
        for data in row:
            if data == '.':
                full = False

    return (f"Board full : {full}") 

# --- here start the script ---
place(PLAYER_1, 3, 2)
display()
display()
print(is_full()) # return False
"""
for y in range(5):
    for x in range(5):
        place(PLAYER_2, x, y)
display()

print(is_full()) # return True
"""
