import turtle
import random as r
import time

hints = 0
movetrtls = []
spawn = 0
kills = 0
screen=turtle.Screen()
screen.title("Chesslike")
screen.bgcolor("grey")
screen.bgpic("game/chessdungeon.gif")
screen.addshape("game/WhitePawn.gif")
screen.addshape("game/BlackPawn.gif")
screen.addshape("game/BlackKnight.gif")
screen.addshape("game/BlackBishop.gif")


screen.setup(width=700, height=700)
screen.tracer(0)

print("Spawning player")
player=turtle.Turtle()
player.shape("game/WhitePawn.gif")
# player.color("green")
player.penup()
player.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
playerpiece = "pawn"
print("Spawned player")
enemy = []


def enemySpawn():
    global player, enemy
    newguy =turtle.Turtle()
    seed = r.randint(0,9)
    if seed < 5:
        newguy.piece = "pawn"
        newguy.shape("game/BlackPawn.gif")
    elif seed < 8:
        newguy.piece = "knight"
        newguy.shape("game/BlackKnight.gif")
    else:
        newguy.piece = "bishop"
        newguy.shape("game/BlackBishop.gif")
    newguy.penup()
    newguy.goto(player.xcor(),player.ycor())
    while player.distance(newguy) == 0:
        newguy.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
    enemy.append(newguy)

def enemyKill():
    global player, kills
    for e in enemy:
        if e.distance(player) == 0:
            e.ht()
            enemy.remove(e)
            kills += 1

print("Spawning enemy 1")
enemySpawn()
print("Spawned enemy 1")


pawn = [[-80,0],[-80,80],[0,80],[80,80],[80,0],[80,-80],[0,-80],[-80,-80]]
knight = [[-80,160],[80,160],[160,80],[160,-80],[80,-160],[-80,-160],[-160,80],[-160,-80]]
bishop = []
rook = []
queen = []
for i in range(1,7):
    for xy in pawn:
        queen.append([xy[0]*i,xy[1]*i])
        if abs(xy[0]) == abs(xy[1]):
            bishop.append([xy[0]*i,xy[1]*i])
        elif xy[0] == 0 or xy[1] == 0:
            rook.append([xy[0]*i,xy[1]*i])
for i in range(len(queen)):
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
    elif piece == "bishop":
        return bishop
    elif piece == "rook":
        return rook
    elif piece == "queen":
        return queen





def enemyMove(emy,piece="pawn"):
    global screen, player
    kill = 0
    badmoves = []
    validmove = 0
    piecearr = pieceArr(piece)
    while not validmove:
        weights = []
        print("Assigning weights")
        for xy in piecearr:
            x = emy.xcor() + xy[0]
            y = emy.ycor() + xy[1]
            weights.append((800-player.distance(x,y)))
            print("Generating move")
        seed = r.choices(piecearr,weights)
        for b in badmoves:
            while seed[0] == b:
                print("Regen bad move")
                seed = r.choices(piecearr,weights)
        x = emy.xcor() + seed[0][0]
        y = emy.ycor() + seed[0][1]
        print("Generated move")
        conflict = 0
        print("Checking conflicts")
        for e in enemy:
            if e.xcor() == x and e.ycor() == y:
                conflict = 1
                print("Conflict found")
        print("Checking to see if I can kill player")
        for xy in piecearr: 
            if player.xcor() == emy.xcor()+xy[0] and player.ycor() == emy.ycor()+xy[1]:
                print("Kill move found")
                kill = 1
                x = emy.xcor() + xy[0]
                y = emy.ycor() + xy[1]
        if not(x > 280 or y > 280 or x < -280 or y < -280 or conflict):
            print("Valid move found")
            validmove = 1
        else:
            print("Invalid move, checking for bad moves")
            for move in piecearr:
                conf = 0
                x = emy.xcor() + move[0]
                y = emy.ycor() + move[1]
                for e in enemy:
                    if e.xcor() == x and e.ycor() == y or x > 280 or y > 280 or x < -280 or y < -280:
                        conf = 1
                if conf:
                    print("Removing bad move")
                    badmoves.append(move)
            if len(badmoves) == len(piecearr):
                print("No good moves, staying in place")
                x = emy.xcor()
                y = emy.ycor()
                validmove = 1
    time.sleep(0.5)
    emy.goto(x, y)
    screen.update()
    if kill:
        player.ht()
        screen.update()
        time.sleep(1)
        resetGame()
        return True




def click(x, y):
    global player, hints, spawn, playerpiece, kills, screen
    if player.distance(x,y) < 40:
        if not hints:
            hints = 1
            piecearr = pieceArr(playerpiece)
            for i in range(len(piecearr)):
                tx = player.xcor()
                ty = player.ycor()
                nx = piecearr[i][0]
                ny = piecearr[i][1]
                x = tx + nx
                y = ty + ny
                for obst in enemy:
                    if obst.xcor() == x and obst.ycor() == y:
                        pass
                if x > 280 or y > 280 or x < -280 or y < -280:
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
                    if enemyMove(en,en.piece):
                        break
                    print("Moved enemy", o)
                if spawn == 5 or len(enemy) == 0:
                    spawn = 0
                    for i in range(round(kills/3)+1-len(enemy)):
                        time.sleep(0.25)
                        print("Spawning enemy",i+1)
                        enemySpawn()
                        screen.update()
                else:
                    spawn += 1


def resetGame():
    global player, enemy, screen, kills, spawn
    player.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
    for e in enemy:
        e.ht()
        enemy.remove(e)
    kills = 0
    spawn = 0
    playerpiece = "pawn"
    player.st()
    enemySpawn()
    screen.update()



screen.listen()
screen.onclick(click)

while True:
    screen.update()
