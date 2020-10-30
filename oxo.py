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
        y+=1
        for data in row:
            txt += data
        txt += "\n"
    print(txt)

def place(carac):
    x = input("x : ")
    y = input("y : ")
    if board[y][x] != ".":
        print("Invalid input")
        place()
    else:
        board[y][x] = carac
    
    return board

def show(x,y):
    return print(board[y][x])

def reset_board():
    #pour chaque ligne du tableau
    for n in range(len(board)):
        #on supprime une ligne
        del board[0]
        #on en rajoute une
        board.append([".", ".", ".", ".", "."])

def isBoardEmpty():
    full = True
    for row in board:
        for data in row:
            if data == ".":
                full == False

    return full
# --- here start the script ---


# display()



# show()


display()
print(isBoardEmpty())
reset_board()
display()
print(isBoardEmpty())