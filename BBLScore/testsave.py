import json
import bbl
bbl.dummys()
obstrs = []
decoded = []
f = open("playerstats.json","r")
obstrs = f.read().split("\n")
for i in obstrs:
    decodedobj = json.JSONDecoder().decode(i)
    for p in bbl.players:
        if decodedobj["name"] == p.name:
            k = decodedobj["batstats"]
            p.batstats = k
            print(p.batstats)
