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
    column = input("Quelle colonne? --->(0-4): ")
    column = int(column)
    
    row = input("Quelle ligne? \/ (0-4): ")
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

def load():
    global oxo_data
    oxo_data = open("oxo.txt")
    data = oxo_data.read()
    oxo_data.close()
    data = data.split('\n')
    
    for row in data:
        
        del board[0]
        new_row = []

        for item in row:
            new_row.append(item)
        board.append(new_row)
def save():
    data = ""
    for row in board:
        for item in row:
            data += item
        data += '\n'
    data = data[:-1]

    oxo_data = open("oxo.txt", "w")
    oxo_data.write(data)
    oxo_data.close()

# --- here start the script ---
load()
display()

turn = 0
print("-= Init Round =-")
x, y = play()
while True:
    
    while turn == 0:            
        
        
        place(PLAYER_1, x, y)
        display()
        
        turn = 1

    while turn == 1 and check_victory(x, y) == False and is_full() == False:
        print("-= Player Two =-")
        player = "Player Two"
        x, y = play()
        place(PLAYER_2, x, y)
        display()
        check_victory(x, y)
        save()
        turn = 2
    while turn == 2 and check_victory(x, y) == False and is_full() == False:
        print("-= Player One =- ")
        player = "Player One"
        x, y = play()
        place(PLAYER_1, x, y)
        display()
        check_victory(x, y)
        save()
        turn = 1
    if check_victory(x, y) == True:
        print(f"{player} Wins !")
        save()
        break

