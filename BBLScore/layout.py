import sys
import random
import bbl
from playerclass import Player
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.tabs = QtWidgets.QTabWidget()
        self.edittab = QtWidgets.QWidget()
        self.playtab = QtWidgets.QWidget()
        self.statstab = QtWidgets.QWidget()

        self.statlist = QtWidgets.QListWidget() # edit tab
        self.textbox = QtWidgets.QLineEdit()
        self.addbutton = QtWidgets.QPushButton("Add Player")
        self.teambtn = QtWidgets.QCheckBox("Team 2")
        self.pitcherbtn = QtWidgets.QCheckBox("Pitcher")

        self.statspcb = QtWidgets.QComboBox() #stats tab
        self.team1lst = QtWidgets.QListWidget()
        self.team2lst = QtWidgets.QListWidget()
        self.team1lst.addItem("Team 1:")
        self.team2lst.addItem("Team 2:")
                                            #play tab

        self.pitchlist = QtWidgets.QComboBox()
        self.pitchtotext = QtWidgets.QLabel("Pitches to:")
        self.inningtext = QtWidgets.QLabel("Inning:1")
        self.outstext = QtWidgets.QLabel("Outs this inning:")
        self.teambattingtext = QtWidgets.QLabel("Team batting:1")
        self.scoretext = QtWidgets.QLabel("Score: 0 , 0")
        self.on1 = QtWidgets.QLabel(" is on First Base")
        self.on1a=QtWidgets.QPushButton("Advance 1st Base")
        self.on2 = QtWidgets.QLabel(" is on Second Base")
        self.on2a=QtWidgets.QPushButton("Advance 2nd Base")
        self.on3 = QtWidgets.QLabel(" is on Third Base")
        self.on3a=QtWidgets.QPushButton("Advance 3rd Base")
        self.out1=QtWidgets.QPushButton(" Gets Out at First")
        self.out2=QtWidgets.QPushButton(" Gets Out at Second")
        self.out3=QtWidgets.QPushButton(" Gets Out at Third")
        self.bbbtn=QtWidgets.QPushButton("Base on Balls(Walk)")
        self.hbpbtn=QtWidgets.QPushButton("Hit By Pitch")
        self.batlist = QtWidgets.QComboBox()
        self.baselist = QtWidgets.QComboBox()
        self.hitstotext = QtWidgets.QLabel("Hits a")
        self.soutbtn = QtWidgets.QPushButton("Strikeout")
        self.outbtn = QtWidgets.QPushButton("Out")

        self.tabs.addTab(self.edittab,"Edit Mode")
        self.tabs.addTab(self.playtab,"Play Mode")
        self.tabs.addTab(self.statstab,"Stats Mode")

        self.edittab.layout = QtWidgets.QGridLayout(self) ####edit tab
        self.edittab.setLayout(self.edittab.layout)
        self.edittab.layout.addWidget(self.team1lst,2,0)
        self.edittab.layout.addWidget(self.team2lst,2,1)
        self.edittab.layout.addWidget(self.textbox,0,0,2,1)
        self.edittab.layout.addWidget(self.addbutton,0,1,2,1)
        self.edittab.layout.addWidget(self.teambtn,0,2)
        self.edittab.layout.addWidget(self.pitcherbtn,1,2)

        self.statstab.layout = QtWidgets.QVBoxLayout(self)#stats tab
        self.statstab.setLayout(self.statstab.layout)
        self.statstab.layout.addWidget(self.statspcb)
        self.statstab.layout.addWidget(self.statlist)
                                                        #play tab
        self.playtab.layout = QtWidgets.QGridLayout(self)
        self.playtab.setLayout(self.playtab.layout)
        self.playtab.layout.addWidget(self.inningtext,0,0)
        self.playtab.layout.addWidget(self.outstext,0,1)
        self.playtab.layout.addWidget(self.teambattingtext,0,2)
        self.playtab.layout.addWidget(self.scoretext,0,3)
        self.playtab.layout.addWidget(self.pitchlist,1,0)
        self.playtab.layout.addWidget(self.pitchtotext,1,1)
        self.playtab.layout.addWidget(self.batlist,1,2)
        self.playtab.layout.addWidget(self.hitstotext,1,3)
        self.playtab.layout.addWidget(self.baselist,1,4)
        self.playtab.layout.addWidget(self.soutbtn,2,3)
        self.playtab.layout.addWidget(self.outbtn,2,4)
        self.playtab.layout.addWidget(self.bbbtn,3,3)
        self.playtab.layout.addWidget(self.hbpbtn,3,4)
        self.playtab.layout.addWidget(self.on1,3,0)
        self.playtab.layout.addWidget(self.on1a,4,0)
        self.playtab.layout.addWidget(self.on2,3,1)
        self.playtab.layout.addWidget(self.on2a,4,1)
        self.playtab.layout.addWidget(self.on3,3,2)
        self.playtab.layout.addWidget(self.on3a,4,2)
        self.playtab.layout.addWidget(self.out1,5,0)
        self.playtab.layout.addWidget(self.out2,5,1)
        self.playtab.layout.addWidget(self.out3,5,2)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        self.textbox.returnPressed.connect(self.addedit)
        self.addbutton.clicked.connect(self.addedit)
        self.statspcb.activated.connect(self.playercb)
        self.baselist.activated.connect(self.hitreg)
        self.on1a.clicked.connect(lambda:self.advancebtns(1))
        self.on2a.clicked.connect(lambda:self.advancebtns(2))
        self.on3a.clicked.connect(lambda:self.advancebtns(3))
        self.baselist.addItems(["Single","Double","Triple","Home Run"])
    @QtCore.Slot()
    def playercb(self):
        self.statlist.clear()
        self.statlist.addItem("Batting Statistics")
        for p in bbl.players:
            if p.name == str(self.statspcb.currentText()):
                for key in p.batstats.keys():
                    self.statlist.addItem(str(key) + ":" + str(p.batstats[key]))
                self.statlist.addItem("\n"+"Pitching Statistics")
                for key in p.pitchstats.keys():
                    self.statlist.addItem(str(key) + ":" + str(p.pitchstats[key]))

    def addedit(self):
        if self.teambtn.isChecked() and len(self.textbox.text())>0 :
            bbl.addPlayer(self.textbox.text().upper().strip(),2,self.pitcherbtn.isChecked())
        elif not self.teambtn.isChecked() and len(self.textbox.text())>0 :
            bbl.addPlayer(self.textbox.text().upper().strip(),1,self.pitcherbtn.isChecked())
        self.textbox.clear()
        self.statspcb.clear()
        self.team1lst.clear()
        self.team2lst.clear()
        self.pitchlist.clear()
        self.batlist.clear()
        self.team1lst.addItem("Team 1:")
        self.team2lst.addItem("Team 2:")
        # print(len(bbl.players))
        for player in bbl.players:
            self.statspcb.addItem(player.name)
            if player.isPitcher and player.team != bbl.teambatting:
                self.pitchlist.addItem(player.name)
        for player in bbl.team1:
            self.team1lst.addItem(player.name)
            if bbl.teambatting == 1:
                self.batlist.addItem(player.name)
        for player in bbl.team2:
            self.team2lst.addItem(player.name)
            if bbl.teambatting == 2:
                self.batlist.addItem(player.name)

    def hitreg(self):
        for p in bbl.players:
            if self.batlist.currentText() == p.name:
                bbl.hit(p,self.baselist.currentIndex()+1,self.pitchlist.currentText())
        if self.batlist.currentIndex()+1 == self.batlist.count():
            self.batlist.setCurrentIndex(-1)
        self.batlist.setCurrentIndex(self.batlist.currentIndex()+1)
        self.updateScore()
        self.updateBases()
    def updateBases(self):
        self.on1.setText("First Base is Empty")
        self.on2.setText("Second Base is Empty")
        self.on3.setText("Third Base is Empty")
        self.out1.setText("First Base is Empty")
        self.out2.setText("Second Base is Empty")
        self.out3.setText("Third Base is Empty")
        for p in bbl.players:
            if p.base == 1:
                self.on1.setText(p.name+" is on First Base")
                self.out1.setText(p.name+" Gets Out at First")
            elif p.base == 2:
                self.on2.setText(p.name+" is on Second Base")
                self.out2.setText(p.name+" Gets Out at Second")
            elif p.base == 3:
                self.on3.setText(p.name+" is on Third Base")
                self.out3.setText(p.name+" Gets Out at Third")
    def advancebtns(self,num):
        for p in bbl.players:
            if p.base == num:
                bbl.advance(p,"advance on base",self.pitchlist.currentText(),1)
        updateScore()
        updateBases()
    def updateScore(self):
        self.outstext.setText("Outs this inning:"+str(bbl.thisInningOuts))
        self.scoretext.setText("Score:"+str(bbl.score[0])+","+str(bbl.score[1]))
if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
