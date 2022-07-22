import turtle
import random as r
import time
hp = 1
hints = 0
movetrtls = []
spawn = 0
kills = 0
screen=turtle.Screen()
screen.title("ChessLike")
screen.bgcolor("grey")
screen.bgpic("game/chessdungeon.gif")
screen.addshape("game/WhitePawn.gif")
screen.addshape("game/WhiteKnight.gif")
screen.addshape("game/WhiteBishop.gif")
screen.addshape("game/WhiteRook.gif")
screen.addshape("game/WhiteQueen.gif")
screen.addshape("game/BlackPawn.gif")
screen.addshape("game/BlackKnight.gif")
screen.addshape("game/BlackBishop.gif")
screen.addshape("game/BlackRook.gif")
screen.addshape("game/BlackQueen.gif")
screen.addshape("game/Marker2.gif")


screen.setup(width=1000, height=700)
screen.tracer(0)

ui = turtle.Turtle()
ui.penup()
ui.ht()
ui.color("black")
ui.goto(410,250)
ui.pendown()
ui.write("{} HP".format(hp), align="center", font=("Pixeloid Sans", 30))
pawnselect = turtle.Turtle()
pawnselect.penup()
pawnselect.shape("game/WhitePawn.gif")
pawnselect.goto(400,180)
knightselect = turtle.Turtle()
knightselect.penup()
knightselect.shape("game/WhiteKnight.gif")
knightselect.goto(400,100)
bishopselect = turtle.Turtle()
bishopselect.penup()
bishopselect.shape("game/WhiteBishop.gif")
bishopselect.goto(400,20)
rookselect = turtle.Turtle()
rookselect.penup()
rookselect.shape("game/WhiteRook.gif")
rookselect.goto(400,-60)
queenselect = turtle.Turtle()
queenselect.penup()
queenselect.shape("game/WhiteQueen.gif")
queenselect.goto(400,-140)

def uiUpdate():
    ui.clear()
    ui.write("{} HP".format(hp), align="center", font=("Pixeloid Sans", 30))
    pawnselect.st()
    knightselect.ht()
    bishopselect.ht()
    rookselect.ht()
    queenselect.ht()
    if hp >= 3:
        knightselect.st()
        bishopselect.st()
    if hp >= 5:
        rookselect.st()
    if hp >= 9:
        queenselect.st()

uiUpdate()

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
    newguy.color(r.choice(["red","orange red","orange","gold","yellow","lime","green","cyan","light blue","blue","medium slate blue","dark violet","magenta","deep pink"]))
    newguy.pensize(10)
    seed = r.randint(0,14)
    if seed < 7:
        newguy.piece = "pawn"
        newguy.shape("game/BlackPawn.gif")
    elif seed < 10:
        newguy.piece = "knight"
        newguy.shape("game/BlackKnight.gif")
    elif seed < 13:
        newguy.piece = "bishop"
        newguy.shape("game/BlackBishop.gif")
    else:
        newguy.piece = "rook"
        newguy.shape("game/BlackRook.gif")
    newguy.penup()
    newguy.goto(player.xcor(),player.ycor())
    while player.distance(newguy) == 0:
        newguy.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
    for e in enemy:
            while e.distance(newguy) == 0:
               newguy.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
    enemy.append(newguy)

def enemyKill():
    global player, kills
    for e in enemy:
        if e.distance(player) == 0:
            e.clear()
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
for i in range(1,8):
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
    t.shape("game/Marker2.gif")
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
    emy.clear()
    emy.pendown()
    emy.goto(x, y)
    emy.penup()
    screen.update()
    if kill:
        player.ht()
        screen.update()
        time.sleep(1)
        screen.update()
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
                stops = []
                no = 0
                if x > 280 or y > 280 or x < -280 or y < -280 or no:
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
                ded = 0
                for en in enemy:
                    o+=1
                    print("Moving enemy",o)
                    if enemyMove(en,en.piece):
                        ded = 1
                        break
                    print("Moved enemy", o)
                if spawn == 5 or len(enemy) == 0 and not ded:
                    spawn = 0
                    for i in range(round(kills/3)+1-len(enemy)):
                        time.sleep(0.25)
                        print("Spawning enemy",i+1)
                        enemySpawn()
                        screen.update()
                elif not ded:
                    spawn += 1


def resetGame():
    global player, enemy, screen, kills, spawn, playerpiece
    player.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
    print("there are",len(enemy), "enemies")
    lemy = len(enemy)
    for i in range(lemy):
        print("lemy ==",lemy)
        enemy[i-1].clear()
        enemy[i-1].ht()
        enemy.pop(i-1)
        print("Removed enemy",i+1)
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
