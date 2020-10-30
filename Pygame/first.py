# Write your code here :-)
hero = Actor("boy")
box = Actor("box")

WIDTH = 500
HEIGHT = 500

hero.bottom = 445
hero.left = 1
box.bottom = 445
box.left = 200
speed_x = 0
speed_y = 0

def draw():

    screen.blit("bg2",(0,0))
    screen.draw.text("Hello la famille", (10,10), fontsize = 34)
    hero.draw()
    box.draw()
def update():
    hero.left += speed_x
    hero.top += speed_y

    if hero.left >= 500:
        hero.left = 0
    if hero.left < 0:
        hero.left = 500
    if hero.bottom >= 445:
        hero.bottom = 445
    if hero.bottom < 0:
        hero.bottom = 0
def on_key_down(key):
    global speed_x
    global speed_y
    if key == keys.RIGHT:
        hero.image = "boy"
        speed_x = 2
    if key == keys.LEFT:
        hero.image = "boy-flip"
        speed_x = -2
    if key == keys.SPACE:
        speed_y = -2

def on_mouse_down(pos):
    if box.collidepoint(pos):
        box.image = "skeleton-fish"


def on_key_up(key):
    global speed_x
    global speed_y
    if key == keys.RIGHT:
        speed_x = 0
    if key == keys.LEFT:
        speed_x = 0
    if key == keys.SPACE:
        speed_y = 2

