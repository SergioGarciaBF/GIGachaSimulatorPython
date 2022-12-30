import csv

#Classe Banner:
class charBanner():
    def __init__(self):
        self.items = []
    
    def loadBanner (self):
        for i in range (3):
            with open(f'./data/{i+3}Stars.csv', mode='r', encoding='utf-8') as archive:
                open_archive = csv.reader(archive, delimiter=',')
                archive_list = []
                for line in (open_archive):
                    archive_list.append(line[0])
                self.items.append(archive_list)