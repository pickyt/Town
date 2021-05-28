import json
from playerclass import Player
import sys
from PySide6 import QtCore, QtWidgets, QtGui

players = []
team1 = []
team2 = []
thisInningOuts = 0
playernames = []
inning = 0
teambatting = 1
score = [0,0]
loadFromFile = True


def inningIncrement(pitcher):
    print("inning : ",inning)
#     if inning == 0:
#         pitcher.pitchstats["IP"]+=1
#     if thisInningOuts==3:
#         inning += 0.5
#         swapTeams()
#         pitcher.pitchstats["IP"]+=1
#         thisInningOuts=0

def addPlayer(name,team,pitcher):
    if name not in playernames:
        players.append(Player(name,team,pitcher))
        playernames.append(players[-1].name)
        if team == 1:
            team1.append(players[-1])
        if team == 2:
            team2.append(players[-1])

def hit(batter,base,pitcher):
    pitch = 0
    for p in players:
        if p.name == pitcher:
            pitch = p
    batter.base = base
    batter.batstats["Hits"]+=1
    if base == 1 :
        batter.batstats["Singles"]+=1
    if base == 2 :
        batter.batstats["Doubles"]+=1
    if base == 3 :
        batter.batstats["Triples"]+=1
    if base == 4 :
        batter.batstats["Home Runs"]+=1
    inningIncrement(pitch)
    advance(batter,"hit",pitch,base)


def advance(batter,type,pitcher,base):
    for p in players:
        if p.name == pitcher:
            pitch = p
    batter.batstats["At Bats"]+=1
    for p in players:
        if p.base>0:
            p.base+=base
        batter.base += base
        if p.base > 3:#reaches home
            print(f"{p.name} made it home")
            score[teambatting-1] += 1
            batter.batstats["RBI"]+=1
            p.batstats["Runs"]+=1
            if p.name == pitcher:
                pitch = p
                pitch.pitchstats["Earned Runs"]+=1
            p.base = 0
    updatepcts()

def swapTeams():
    if teambatting == 1:
        teambatting = 2
    else:
        teambatting = 1
def strikeout(batter,pitcher):
    inningIncrement(pitcher)
    batter.base = 0
    pitcher.pitchstats["K"]+=1
    thisInningOuts+=1
def out(batter):
    batter.base = 0
    thisInningOuts+=1
def updatepcts():
    for p in players:
        p.batstats["Batting Avg"] = div(p.batstats["Hits"],p.batstats["At Bats"])
        p.batstats["On Base %"] = div((p.batstats["Hits"]+p.batstats["Walks"]),p.batstats["At Bats"])
        p.batstats["Tot Bases"] = p.batstats["Singles"] + 2* p.batstats["Doubles"]+3*p.batstats["Triples"]+4*p.batstats["Home Runs"]
        p.batstats["Slugging"] = div(p.batstats["Total Bases"],p.batstats["At Bats"])
        p.batstats["OPS"] = p.batstats["On Base %"] + p.batstats["Slugging"]
        p.pitchstats["ERA"]= div((9 * p.pitchstats["Earned Runs"]),p.pitchstats["IP"])
        p.pitchstats["WHIP"]= div(p.pitchstats["Walks"]+p.pitchstats["Hits Against"],p.pitchstats["IP"])
        saveplayers()

def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0

def saveplayers():
    jsonFile = open("playerstats.json", "w")
    for p in players:
        jsonStr = json.dumps(p.__dict__)
        jsonFile.write(jsonStr+"\n")
def loadplayers():
    jsonFile =  open("playerstats.json", "r")
    f = jsonFile.read().split("\n")
def dummys(num):
    for i in range(1,num):
        if i==1:
            addPlayer(f'pitcher{i}',1,True)
            addPlayer(f'pitcher{i}',2,True)
dummys(9)
for p in players:
    print(p.name)
