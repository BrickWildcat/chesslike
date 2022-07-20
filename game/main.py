import turtle
import random as r
import time
hints = 0
movetrtls = []


screen=turtle.Screen()
screen.title("Chesslike")
screen.bgcolor("grey")
screen.bgpic("checkerboard.gif")
screen.addshape("pawn.gif")
screen.addshape("tempawn.gif")


screen.setup(width=400, height=400)
screen.tracer(0)

print("Spawning player")
player=turtle.Turtle()
player.shape("pawn.gif")
# player.color("green")
player.penup()
player.goto(120, -120)
print("Spawned player")
enemy = []


def enemySpawn():
    global player, enemy
    newguy =turtle.Turtle()
    newguy.shape("tempawn.gif")
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


mtpos = [[-80,0],[-80,80],[0,80],[80,80],[80,0],[80,-80],[0,-80],[-80,-80]]
for i in range(8):
    movetrtls.append(turtle.Turtle())
for t in movetrtls:
    t.penup()
    t.shape("circle")
    t.shapesize(1.5)
    t.color("red")
    t.ht()


def enemyMove(emy):
    validmove = 0
    while not validmove:
        weights = []
        for xy in mtpos:
            x = emy.xcor() + xy[0]
            y = emy.ycor() + xy[1]
            weights.append((340-player.distance(x,y))*10)
        seed = r.choices(mtpos,weights)
        x = emy.xcor() + seed[0][0]
        y = emy.ycor() + seed[0][1]
        conflict = 0
        for e in enemy:
            if e.xcor() == x and e.ycor() == y:
                conflict = 1
        for xy in mtpos: 
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
    global player, hints
    if player.distance(x,y) < 40:
        if not hints:
            hints = 1
            for i in range(8):
                tx = player.xcor()
                ty = player.ycor()
                nx = mtpos[i][0]
                ny = mtpos[i][1]
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
                player.goto(t.xcor(),t.ycor())
                enemyKill()
                hints = 0
                for t in movetrtls:
                    t.ht()
                screen.update()
                o=0
                for en in enemy:
                    o+=1
                    print("Moving enemy",o)
                    enemyMove(en)
                    print("Moved enemy", o)
                break



screen.listen()
screen.onclick(click)
for t in movetrtls:
    screen.onclick(click)

while True:
    screen.update()
