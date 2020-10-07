from microbit import *

PLAYER1 = 1
PLAYER2 = 2

PLAYER1_INTENSITY = 9
PLAYER2_INTENSITY = 5
board = []

def board_initialize():
    for y in range(5):
        row = []
        for x in range(5):
            row.append(0)
        board.append(row)


def check_victory(x, y, player):
    if x < 4 and board[x+1][y] == player:
        if x < 3 and board[x+2][y] == player:
            return True
    return False


# data = xyn (n=player number)
def set_pixel(data):
    x = chr(data[0])
    x = int(x)

    y = chr(data[1])
    y = int(y)

    player_number = chr(data[2])
    player_number = int(player_number)

    if board[x][y] > 0:
        return "NOT OK"
    else:
        board[x][y] = player_number
        if check_victory(x, y, player_number):
            return "WIN"
        return "OK"


def display_board():
    # lire le tableau (board) et afficher pour chaque élément soit
    # l'intensité du joueur1 soit celle du joueur2 ou rien si 0.
    display.clear()
    for x in range(5):
        for y in range(5):
            value = board[x][y]
            if value > 0:
                if value == PLAYER1:
                    intensity = PLAYER1_INTENSITY
                else:
                    intensity = PLAYER2_INTENSITY
                display.set_pixel(x, y, intensity)


board_initialize()

while True:
    data = uart.read()
    if data:
        result = set_pixel(data)
        if result == "WIN":
            display.show(Image.HAPPY)
        print(result)
        display_board()


