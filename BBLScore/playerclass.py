import json
class Player:
    def __init__(self,name,team,pitcher):
        self.name = name
        self.team = team
        self.isPitcher = pitcher
        self.base = 0
        self.batstats = {
        "Batting Avg" : .0,
        "On Base %" : .0,
        "Slugging" : .0,
        "OPS" : .0,
        "At Bats":0,
        "Hits" : 0,
        "Runs" :0,
        "Singles" : 0,
        "Doubles" : 0,
        "Triples" : 0,
        "Home Runs" : 0,
        "Total Bases" : 0,
        "Walks" :0,
        "RBI" : 0,
        "Wins" : 0,
        "Games Played":0
        }

        self.pitchstats = {
         "ERA" : .0,
         "WHIP": .0,
         "K":0,
         "Hits Against":0,
         "Walks":0,
         "IP":0,
         "Earned Runs":0
        }
