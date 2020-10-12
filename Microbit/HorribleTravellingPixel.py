from microbit import*
x=0
y=0
dx=1
dy=0

while True:
        display.clear()
        display.set_pixel(x,y,9)
        sleep(125)
        x+=dx
        y+=dy
        if x>4:
            x=4
            y=1
            dx=0
            dy=1
        if y>4:
            x=3
            y=4
            dx=-1
            dy=0
        if x<0:
            x=0
            y=3
            dx=0
            dy=-1
        if y<0:
            x=1
            y=0
            dx=1
            dy=0
        if x == 0 and y == 1:
            dy=0
            dx=1
            y=1
            x=0
        if x == 3 and y == 1:
            dy=1
            dx=0
            x = 3
            y = 1
        if y == 3 and x == 3:
            dy=0
            dx=-1
            x = 3
            y = 3
        if x == 1 and y == 3:
            dy =-1
            dx = 0
            x = 1
            y = 3
        if x == 1 and y == 2:
            dy = 0
            dx = 1
            x = 1
            y = 2
        if x == 2 and y == 2:
            display.clear()
            display.set_pixel(2, 2, 9)
            sleep(300)

            x = 0
            y = 0
