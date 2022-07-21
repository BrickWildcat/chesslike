import turtle
import random as r
import time
hints = 0
movetrtls = []
spawn = 1

screen=turtle.Screen()
screen.title("Chesslike")
screen.bgcolor("grey")
screen.bgpic("game/checkerboard.gif")
screen.addshape("game/WhitePawn.gif")
screen.addshape("game/BlackPawn.gif")


screen.setup(width=400, height=400)
screen.tracer(0)

print("Spawning player")
player=turtle.Turtle()
player.shape("game/WhitePawn.gif")
# player.color("green")
player.penup()
player.goto(120, -120)
playerpiece = "pawn"
print("Spawned player")
enemy = []


def enemySpawn():
    global player, enemy
    newguy =turtle.Turtle()
    if r.randint(0,2):
        newguy.piece = "pawn"
        newguy.shape("game/BlackPawn.gif")
    else:
        newguy.piece = "knight"
        newguy.shape("square")
        newguy.color("red")
    newguy.penup()
    newguy.goto(player.xcor(),player.ycor())
    while player.distance(newguy) == 0:
        newguy.goto(r.randint(0,3)*80-120, r.randint(0,3)*80-120)
    enemy.append(newguy)

def enemyKill():
    global player
    for e in enemy:
        if e.distance(player) == 0:
            e.ht()
            enemy.remove(e)

print("Spawning enemy 1")
enemySpawn()
print("Spawned enemy 1")
print("Spawning enemy 2")
enemySpawn()
print("Spawned enemy 2")


pawn = [[-80,0],[-80,80],[0,80],[80,80],[80,0],[80,-80],[0,-80],[-80,-80]]
knight = [[-80,160],[80,160],[160,80],[160,-80],[80,-160],[-80,-160],[-160,80],[-160,-80]]
for i in range(8):
    movetrtls.append(turtle.Turtle())
for t in movetrtls:
    t.penup()
    t.shape("circle")
    t.shapesize(1.5)
    t.color("red")
    t.ht()

def pieceArr(piece):
    global pawn, knight
    if piece == "pawn":
        return pawn
    elif piece == "knight":
        return knight



def enemyMove(emy,piece="pawn"):
    validmove = 0
    piecearr = pieceArr(piece)
    while not validmove:
        weights = []
        for xy in piecearr:
            x = emy.xcor() + xy[0]
            y = emy.ycor() + xy[1]
            weights.append((340-player.distance(x,y))*10)
        seed = r.choices(piecearr,weights)
        x = emy.xcor() + seed[0][0]
        y = emy.ycor() + seed[0][1]
        conflict = 0
        for e in enemy:
            if e.xcor() == x and e.ycor() == y:
                conflict = 1
        for xy in piecearr: 
            cft = 0
            for e in enemy:
                if e.xcor() == emy.xcor()+xy[0] and emy.ycor()+xy[1]:
                    cft = 1
            if player.xcor() == emy.xcor()+xy[0] and player.ycor() == emy.ycor()+xy[1] and not cft:
                x = emy.xcor() + xy[0]
                y = emy.ycor() + xy[1]
        if not(x > 120 or y > 120 or x < -120 or y < -120 or conflict):
            validmove = 1
    time.sleep(0.5)
    emy.goto(x, y)
    screen.update()




def click(x, y):
    global player, hints, spawn, playerpiece
    if player.distance(x,y) < 40:
        if not hints:
            hints = 1
            piecearr = pieceArr(playerpiece)
            for i in range(8):
                tx = player.xcor()
                ty = player.ycor()
                nx = piecearr[i][0]
                ny = piecearr[i][1]
                x = tx + nx
                y = ty + ny
                if x > 120 or y > 120 or x < -120 or y < -120:
                    movetrtls[i].ht
                else:
                    movetrtls[i].goto(x,y)
                    movetrtls[i].st()
        else:
            hints = 0
            for t in movetrtls:
                t.ht()
    else:
        for t in movetrtls:
            if t.distance(x,y) < 40 and t.isvisible():
                print("Moving player")
                player.goto(t.xcor(),t.ycor())
                enemyKill()
                hints = 0
                for t in movetrtls:
                    t.ht()
                screen.update()
                print("Moved player")
                o=0
                for en in enemy:
                    o+=1
                    print("Moving enemy",o)
                    enemyMove(en,en.piece)
                    print("Moved enemy", o)
                if spawn == 5 or len(enemy) == 0:
                    time.sleep(0.5)
                    enemySpawn()
                    spawn = 0
                else:
                    spawn += 1



screen.listen()
screen.onclick(click)
for t in movetrtls:
    screen.onclick(click)

while True:
    screen.update()
