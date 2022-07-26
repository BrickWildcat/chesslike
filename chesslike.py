#!/bin/python
import turtle
import tkinter as tk
import random as r
import time
import pickle
import os
os.system("pip install --upgrade playsound")
from playsound import playsound

pckl = open('game/hiscore.pkl', 'rb')
hiscore = pickle.load(pckl)
score = 0
hp = 1
hints = 0
movetrtls = []
moves = []
heart = 0
spawn = 0
kills = 0
screen=turtle.Screen()
icon = tk.Image("photo",file="game/pawn.png")
screen._root.iconphoto(True, icon)
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
screen.addshape("game/HeartB.gif")
screen.addshape("game/Title.gif")
grid = [-280, -200, -120, -40, 40, 120, 200, 280]
ygrd = ["8","7","6","5","4","3","2","1"]
xgrd = ["a","b","c","d","e","f","g","h"]
screen.setup(width=1000, height=700)
screen.tracer(0)

ui = turtle.Turtle()
ui.penup()
ui.ht()
ui.color("black")
ui.goto(410,250)
ui.pendown()
ui.write("{} HP".format(hp), align="center", font=("Pixeloid Sans", 30))
moveui = turtle.Turtle()
moveui.penup()
moveui.ht()
pawnselect = turtle.Turtle()
pawnselect.penup()
pawnselect.shape("game/WhitePawn.gif")
pawnselect.goto(400,180)
pawnselect.piece = "pawn"
knightselect = turtle.Turtle()
knightselect.penup()
knightselect.shape("game/WhiteKnight.gif")
knightselect.goto(400,100)
knightselect.piece = "knight"
bishopselect = turtle.Turtle()
bishopselect.penup()
bishopselect.shape("game/WhiteBishop.gif")
bishopselect.goto(400,20)
bishopselect.piece = "bishop"
rookselect = turtle.Turtle()
rookselect.penup()
rookselect.shape("game/WhiteRook.gif")
rookselect.goto(400,-60)
rookselect.piece = "rook"
queenselect = turtle.Turtle()
queenselect.penup()
queenselect.shape("game/WhiteQueen.gif")
queenselect.goto(400,-140)
queenselect.piece = "queen"

def uiUpdate():
    global hp, score, ui, pawnselect, knightselect, bishopselect, rookselect, queenselect, hiscore
    if score > hiscore:
        hiscore = score
        pckl = open('game/hiscore.pkl','wb')
        pickle.dump(hiscore, pckl)
    ui.clear()
    ui.write("{} HP".format(hp), align="center", font=("Pixeloid Sans", 30))
    ui.pu()
    ui.goto(405,-325)
    ui.pd
    ui.write("Score: {}\nHiScore: {}".format(score, hiscore), align="center", font=("Pixeloid Sans", 16))
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
    ui.goto(410,250)

def printMoves():
    global moves, screen
    moveui.goto(-410,280)
    moveui.clear()
    for m in moves:
        moveui.color(m[0].pencolor())
        moveui.write(m[1], align="center", font=("Pixeloid Sans", 25))
        moveui.goto(-410,moveui.ycor()-40)
    screen.update()

uiUpdate()

# print("Spawning player")
player=turtle.Turtle()
player.shape("game/WhitePawn.gif")
player.color("white")
player.penup()
player.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
player.piece = "pawn"
# print("Spawned player")
enemy = []

def enemySpawn():
    global player, enemy, score
    newguy =turtle.Turtle()
    newguy.color(r.choice(["red","orange red","orange","gold","yellow","lime","green","cyan","light blue","blue","medium slate blue","dark violet","magenta","deep pink"]))
    seed = r.randint(0,999)
    if seed + score < 500:
        newguy.piece = "pawn"
        newguy.shape("game/BlackPawn.gif")
    elif seed + score < 800:
        newguy.piece = "knight"
        newguy.shape("game/BlackKnight.gif")
    elif seed + score < 1100:
        newguy.piece = "bishop"
        newguy.shape("game/BlackBishop.gif")
    elif seed + score < 1450:
        newguy.piece = "rook"
        newguy.shape("game/BlackRook.gif")
    else:
        newguy.piece = "queen"
        newguy.shape("game/BlackQueen.gif")
    newguy.penup()
    newguy.goto(player.xcor(),player.ycor())
    while player.distance(newguy) == 0:
        newguy.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
    for e in enemy:
            while e.distance(newguy) == 0:
               newguy.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
    enemy.append(newguy)

def enemyKill():
    global player, kills, score, hiscore
    for e in enemy:
        if e.distance(player) == 0:
            if e.piece == "pawn":
                score += 10
            elif e.piece == "knight" or e.piece == "bishop":
                score += 30
            elif e.piece == "rook":
                score += 50
            else:
                score += 90
            uiUpdate()
            e.clear()
            e.ht()
            enemy.remove(e)
            kills += 1
            return True
    return False

# print("Spawning enemy 1")
enemySpawn()
# print("Spawned enemy 1")


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

def heartSpawn():
    global heart, player, enemy
    newguy = turtle.Turtle()
    newguy.shape("game/HeartB.gif")
    newguy.penup()
    newguy.goto(player.xcor(),player.ycor())
    while player.distance(newguy) == 0:
        newguy.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
    for e in enemy:
            while e.distance(newguy) == 0:
               newguy.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
    heart = newguy

def isBlocked(trtl,move):
    global player, enemy
    if move[0] != 0:
        loops = abs(move[0]/80)
    else:
        loops = abs(move[1]/80)
    eitx = move[0]/loops
    eity = move[1]/loops
    # print("eitx",eitx)
    # print("eity",eity)
    # print("loops",loops)
    for i in range(1,round(loops)):
        if i != loops:
            x = trtl.xcor()+(i*eitx)
            y = trtl.ycor()+(i*eity)
            for e in enemy:
                if e.distance(x,y) == 0:
                    return True
            if player.distance(x,y) == 0:
                return True
    return False

def enemyMove(emy,piece):
    global screen, player, moves, heart
    kill = 0
    badmoves = []
    if heart != 0:
        badmoves.append([heart.xcor()-emy.xcor(),heart.ycor()-emy.ycor()])
    validmove = 0
    piecearr = pieceArr(piece)
    while not validmove:
        weights = []
        # print("Assigning weights")
        for xy in piecearr:
            x = emy.xcor() + xy[0]
            y = emy.ycor() + xy[1]
            weights.append((800-player.distance(x,y)))
            # print("Generating move")
        seed = r.choices(piecearr,weights)
        for b in badmoves:
            while seed[0] == b:
                # print("Regen bad move")
                seed = r.choices(piecearr,weights)
        x = emy.xcor() + seed[0][0]
        y = emy.ycor() + seed[0][1]
        # print("Generated move")
        conflict = 0
        # print("Checking conflicts")
        conflict = isBlocked(emy,seed[0])
        for e in enemy:
            if e.xcor() == x and e.ycor() == y:
                conflict = 1
                # print("Conflict found")
        # print("Checking to see if I can kill player")
        for xy in piecearr: 
            tx = emy.xcor() + xy[0]
            ty = emy.ycor() + xy[1]
            if player.distance(tx,ty) == 0 and not(isBlocked(emy,xy)):
                # print("Kill move found")
                kill = 1
                x = player.xcor()
                y = player.ycor()
        if not(x > 280 or y > 280 or x < -280 or y < -280 or conflict):
            # print("Valid move found")
            validmove = 1
        else:
            # print("Invalid move, checking for bad moves")
            for move in piecearr:
                conf = isBlocked(emy,move)
                x = emy.xcor() + move[0]
                y = emy.ycor() + move[1]
                for e in enemy:
                    if e.distance(x,y) == 0 or x > 280 or y > 280 or x < -280 or y < -280:
                        conf = 1
                if conf:
                    # print("Removing bad move")
                    badmoves.append(move)
            if len(badmoves) == len(piecearr)+1:
                # print("No good moves, staying in place")
                x = emy.xcor()
                y = emy.ycor()
                validmove = 1
    time.sleep(0.5)
    emy.clear()
    emy.width(5)
    emy.pendown()
    emy.goto(x, y)
    emy.penup()
    screen.update()
    # playsound("game/chessmove.wav")
    if kill:
        player.ht()
        if len(moves) == 16:
            moves.pop(0)
        nxmv = [emy,xgrd[grid.index(emy.xcor())]+ygrd[grid.index(emy.ycor())]]
        nxmv[1] = "x"+nxmv[1]
        if emy.piece == "knight":
            nxmv[1] = "N"+nxmv[1]
        elif emy.piece == "bishop":
            nxmv[1] = "B"+nxmv[1]
        elif emy.piece == "rook":
            nxmv[1] = "R"+nxmv[1]
        elif emy.piece == "queen":
            nxmv[1] = "Q"+nxmv[1]
        moves.append(nxmv)
        printMoves()
        screen.update()
        time.sleep(1)
        screen.update()
        resetGame()
        return True




def click(x, y):
    global player, hints, spawn, kills, screen, heart, hp, score
    if title.isvisible():
        title.ht()
    if player.distance(x,y) < 40:
        if not hints:
            hints = 1
            piecearr = pieceArr(player.piece)
            for i in range(len(piecearr)):
                tx = player.xcor()
                ty = player.ycor()
                nx = piecearr[i][0]
                ny = piecearr[i][1]
                x = tx + nx
                y = ty + ny
                stops = []
                if x > 280 or y > 280 or x < -280 or y < -280 or isBlocked(player,piecearr[i]):
                    movetrtls[i].ht
                else:
                    movetrtls[i].goto(x,y)
                    movetrtls[i].st()
        else:
            hints = 0
            for t in movetrtls:
                t.ht()
    else:
        for t in [pawnselect,knightselect,bishopselect,rookselect,queenselect]:
            if t.distance(x,y) < 40 and t.isvisible() and player.piece != t.piece:
                hints = 0
                for mt in movetrtls:
                    mt.ht()
                player.piece = t.piece
                player.shape(t.shape())
                o=0
                ded = 0
                for en in enemy:
                    o+=1
                    # print("Moving enemy",o)
                    if enemyMove(en,en.piece):
                        ded = 1
                        break
                    # print("Moved enemy", o)
                    if len(moves) == 16:
                        moves.pop(0)
                    nxmv = [en,xgrd[grid.index(en.xcor())]+ygrd[grid.index(en.ycor())]]
                    if en.piece == "knight":
                        nxmv[1] = "N"+nxmv[1]
                    elif en.piece == "bishop":
                        nxmv[1] = "B"+nxmv[1]
                    elif en.piece == "rook":
                        nxmv[1] = "R"+nxmv[1]
                    elif en.piece == "queen":
                        nxmv[1] = "Q"+nxmv[1]
                    moves.append(nxmv)
                    printMoves()
                if spawn == 5 or len(enemy) == 0 and not ded:
                    spawn = 0
                    for i in range(round(kills/5)+2-len(enemy)):
                        time.sleep(0.5)
                        # print("Spawning enemy",i+1)
                        enemySpawn()
                        screen.update()
                    if heart == 0:
                        heartSpawn()
                elif not ded:
                    spawn += 1
        for t in movetrtls:
            if t.distance(x,y) < 40 and t.isvisible():
                # print("Moving player")
                player.goto(t.xcor(),t.ycor())
                nxmv = [player,xgrd[grid.index(player.xcor())]+ygrd[grid.index(player.ycor())]]
                if enemyKill():
                    nxmv[1] = "x"+nxmv[1]
                if len(moves) == 16:
                    moves.pop(0)
                if player.piece == "knight":
                  nxmv[1] = "N"+nxmv[1]
                elif player.piece == "bishop":
                    nxmv[1] = "B"+nxmv[1]
                elif player.piece == "rook":
                    nxmv[1] = "R"+nxmv[1]
                elif player.piece == "queen":
                   nxmv[1] = "Q"+nxmv[1]
                moves.append(nxmv)
                printMoves()
                hints = 0
                for t in movetrtls:
                    t.ht()
                screen.update()
                # playsound("game/chessmove.wav")
                # print("Moved player")
                if heart != 0:
                    if player.distance(heart) == 0:
                        hp += 1
                        score += 5*(hp-1)
                        uiUpdate()
                        heart.ht()
                        screen.update()
                        heart = 0
                o=0
                ded = 0
                for en in enemy:
                    o+=1
                    # print("Moving enemy",o)
                    if enemyMove(en,en.piece):
                        ded = 1
                        break
                    # print("Moved enemy", o)
                    if len(moves) == 16:
                        moves.pop(0)
                    nxmv = [en,xgrd[grid.index(en.xcor())]+ygrd[grid.index(en.ycor())]]
                    if en.piece == "knight":
                        nxmv[1] = "N"+nxmv[1]
                    elif en.piece == "bishop":
                        nxmv[1] = "B"+nxmv[1]
                    elif en.piece == "rook":
                        nxmv[1] = "R"+nxmv[1]
                    elif en.piece == "queen":
                        nxmv[1] = "Q"+nxmv[1]
                    moves.append(nxmv)
                    printMoves()
                if spawn == 5 or len(enemy) == 0 and not ded:
                    spawn = 0
                    for i in range(round(kills/4)+1-len(enemy)):
                        # print("Spawning enemy",i+1)
                        enemySpawn()
                        time.sleep(0.5)
                        screen.update()
                    if heart == 0:
                        heartSpawn()
                elif not ded:
                    spawn += 1


def resetGame():
    global player, enemy, screen, kills, spawn, moves, moveui, heart, hp, movetrtls, score
    for t in movetrtls:
        t.ht()
    player.goto(r.randint(-2,5)*80-120, r.randint(-2,5)*80-120)
    # print("there are",len(enemy), "enemies")
    lemy = len(enemy)
    for i in range(lemy-1,-1,-1):
        # print(i)
        enemy[i].clear()
        enemy[i].ht()
        enemy.pop(i)
        # print("Removed enemy",i+1)
    spawn = 0
    if heart != 0:
        heart.ht()
        heart = 0
    if hp>1:
        hp -= 1
        score -= round(10*(1.3**hp))
        kills = hp
        if hp < 3 and (player.piece == "bishop" or player.piece == "knight"):
            player.piece = "pawn"
            player.shape("game/WhitePawn.gif")
        elif hp < 5 and (player.piece == "rook"):
            player.piece = "bishop"
            player.shape("game/WhiteBishop.gif")
        elif hp < 9 and (player.piece == "queen"):
            player.piece = "rook"
            player.shape("game/WhiteRook.gif")
        enemySpawn()
        uiUpdate()
    else:
        moves = []
        moveui.clear()
        kills = 0
        score = 0
        player.piece = "pawn"
        player.shape("game/WhitePawn.gif")
        enemySpawn()
        uiUpdate()
        title.st()
    player.st()
    screen.update()
screen.listen()
screen.onclick(click)

title = turtle.Turtle()
title.shape("game/Title.gif")
title.goto(0,0)

starttime = time.time_ns() - (38.4*(10**9))
while True:
    screen.update()
    if time.time_ns()-starttime >= 38.4*(10**9):
        playsound("game/Song.wav", 0)
        starttime = time.time_ns()
