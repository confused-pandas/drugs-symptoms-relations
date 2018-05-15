import couchdb


class OrphaDataManager:

    def __init__(self, item):
        self.item = item
        self.couchServer = couchdb.Server('http://couchdb.telecomnancy.univ-lorraine.fr')
        self.dbname = 'orphadatabase'
        self.db = self.couchServer[self.dbname]
        self.view_cs = 'clinicalsigns/GetDiseaseByClinicalSign'
        self.view_disease = 'diseases/GetDiseases'

    def extractNameFromCs(self):
        data_orpha = []
        for elem in self.db.view(self.view_cs, key=self.item):
            value = elem.value
            disease=value["disease"]
            diseaseName = disease["Name"]["text"]
            data_orpha.append(diseaseName)
        return data_orpha


    def extractNameFromId(self):
        diseaseName = ""
        for elem in self.db.view(self.view_disease, key=self.item):
            value = elem.value
            diseaseName = value["Name"]["text"]
        return diseaseName

    
    
        
            
            
manager = OrphaDataManager(1052).extractNameFromId()
print(manager)
#manager = OrphaDataManager("Xerophthalmia/dry eyes")
#print(manager.extractNameFromCs())