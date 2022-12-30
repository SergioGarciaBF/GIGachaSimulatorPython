import modules.Gacha as gG
import csv

#Classe Jogador:
class Player():
    def __init__ (self, playerArchive):
        self.midCont = 0
        self.maxCont = 0
        self.featured4Star = False
        self.featured5Star = False
        self.playerArchive = playerArchive
    
    def constructor (self, midCont, maxCont, featured4Star, featured5Star, playerArchive): #Serve pra nada
        self.midCont = midCont
        self.maxCont = maxCont
        self.featured4Star = featured4Star
        self.featured5Star = featured5Star
        self.playerArchive = playerArchive

    def updateStatePlayer (self, midCont, maxCont, featured4Star, featured5Star):
        self.midCont = midCont
        self.maxCont = maxCont
        self.featured4Star = featured4Star
        self.featured5Star = featured5Star
    
    def loadState (self):
        with open(f'./data/{self.playerArchive}.csv', mode='r', encoding='utf-8') as archive:
            open_archive = csv.reader(archive, delimiter=',')
            for line in (open_archive):
                self.midCont = int(line[0])
                self.maxCont = int(line[1])
                self.featured4Star = bool(line[2])
                self.featured5Star = bool(line[3])

    def saveState (self):
        with open(f'./data/{self.playerArchive}.csv', mode='w', newline='', encoding='utf-8') as archive:
            state = [self.midCont, self.maxCont, self.featured4Star, self.featured5Star]
            csv.writer(archive, delimiter=',').writerow(state)

    def playerSummon(self, times, items):
        #Realizar 180 tentativas de gacha:
        for i in range (times):
            print(f'{i+1:3}: ', end='')
            updates = gG.summon(items, 
                                self.featured4Star, self.featured5Star, 
                                self.maxCont, self.midCont)
            
            #Atualizar o status do jogador:
            self.updateStatePlayer(updates[0], updates[1], updates[2], updates[3])

    def printState(self):
        print(f'''
        -------------------------------------
        Estado do jogador:
        midCont: {self.midCont}
        maxcont: {self.maxCont}
        featured4Stars: {self.featured4Star}
        featured5Stars: {self.featured5Star}
        -------------------------------------
        ''')