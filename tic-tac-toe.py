from random import shuffle

gr = '012345678'
end = False

print("Let's start...")

def show():
 x = 0
 for i in gr:
  if end == True:
   break
  if x > 2:
   x = 0
   print()
  print(i,end=' ')
  x += 1
 print()
 print()


print()

lgr = list(gr)
shuffle(lgr)

def randomx(x):
 for i in range(x):
  global gr
  pick = lgr.pop()
  gr = gr.replace(pick,"X")
  show()
  pick = lgr.pop()
  gr = gr.replace(pick,"O")
  show()
  allrow()


def rows(*args):
 row = ''
 for i in args:
  row += gr[i]
 return row

def allrow():
 global end
 w = "XXX"
 o = "OOO"
 r1 = rows(0,1,2)
 r2 = rows(3,4,5)
 r3 = rows(6,7,8)
 c1 = rows(0,3,6)
 c2 = rows(1,4,7)
 c3 = rows(2,6,8)
 d1 = rows(0,4,8)
 d2 = rows(2,4,6)

 r = (r1,r2,r3,c1,c2,c3,d1,d2)
 if w in r:
  print("X is the winner")
  end = True
 elif o in r:
  print("O is the winner")
  end = True
 else:
  print("The game goes on\n")
  if len(lgr)>1:
   randomx(1)

allrow()