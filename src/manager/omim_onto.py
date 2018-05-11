import csv

class OmimOntoManager:

    def __init__(self, id):
        self.id = id
        self.path = './res/database/omim/omim_onto.csv'

    def extractDataFromOmim(self):
        data_omimc = {}
        with open('./res/database/omim/omim_onto.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            b = False
            while b != True:
                row = csv_reader.__next__()
                a = row[0][42:]
                if a.startswith("MTHU"):
                    if row[0][46:52] == self.id:
                        data_omimc[self.id] = row[5]
                        b = True
                else:
                    if row[0][42:48] == self.id:
                        data_omimc[self.id] = row[5]
                        b = True
        return data_omimc

    def extractDataFromCui(self):
        data_omimc = {}
        with open('./res/database/omim/omim_onto.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            b = False
            while b != True:
                row = csv_reader.__next__()
                a = row[5]
                if a == self.id:
                    if row[0][42:].startswith("MTHU"):
                        data_omimc[self.id] = row[0][46:52]
                        b = True
                    else:
                        data_omimc[self.id] = row[0][42:48]
                        b = True
        return data_omimc




#manager = OmimOntoManager("C1412749")
#print(manager.extractDataFromCui())