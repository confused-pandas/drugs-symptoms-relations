import csv

class OmimOntoManager:

    def __init__(self, omim):
        self.omim = omim
        self.path = './res/database/omim/omim_onto.csv'

    def extractData(self):
        data_omimc = {}
        with open('./res/database/omim/omim_onto.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            b = False
            while b != True:
                row = csv_reader.__next__()
                a = row[0][42:]
                if a.startswith("MTHU"):
                    if row[0][46:52] == self.omim:
                        data_omimc[self.omim] = row[5]
                        b = True
                else:
                    if row[0][42:48] == self.omim:
                        data_omimc[self.omim] = row[5]
                        b = True
        return data_omimc



manager = OmimOntoManager("600374")
print(manager.extractData())