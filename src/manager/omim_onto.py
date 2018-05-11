import csv

class OmimCsvManager:

    def __init__(self, cui):
        self.cui = cui
        self.path = "./res/database/omim/omim_onto.csv"

    def extractData(self):
        data_omimc = {}
        with open(self.path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[5] == self.cui:
                    if row[0][42:].startswith("MTHU"):
                        data_omimc[self.cui] = row[0][46:52]
                    else:
                        data_omimc[self.cui] = row[0][46:52]
            print(data_omimc) 

                    
                
manager = OmimCsvManager("C1412749")
manager.extractData()