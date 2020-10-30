PLAYER_1 = 'X'
PLAYER_2 = 'O'

board = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]]

# --- Functions ---

def play():

    # code qui permet à l'utilisateur de choisir une position valide en x et en y
    column = input("Quelle colonne? (0-4): ")
    column = int(column)
    
    row = input("Quelle ligne? (0-4): ")
    row = int(row)

    while row < 0 or row > 4 or column < 0 or column > 4 or give(column, row) != '.':
        print(f"La coordonnée {column}, {row} est invalide!")
        column = input("Quelle colonne? (0-4): ")
        column = int(column)
        
        row = input("Quelle ligne? (0-4): ")
        row = int(row)

    return column, row


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
    if x < 0 or x > 4 or y < 0 or y > 4:
        return None
    return board[y][x]


def place(carac, x, y):
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


def check_victory(x, y):

    player = give(x, y)

    if give(x + 1, y) == player:
        if give(x + 2, y) == player:
            return True
        if give(x - 1, y) == player:
            return True
    if give(x - 1, y) == player and give(x - 2, y) == player:
        return True

    if give(x, y + 1) == player:
        if give(x, y + 2) == player:
            return True
        if give(x, y - 1) == player:
            return True
    if give(x, y - 1) == player and give(x, y - 2) == player:
        return True


    return False

# --- here start the script ---
place(PLAYER_1, 2, 1)
place(PLAYER_1, 2, 3)
display()

x, y = play()
print(x, y)

place(PLAYER_1, x, y)

display()
print(check_victory(x, y))