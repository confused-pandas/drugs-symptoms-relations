import couchdb

class OrphaDataManager:

    def __init__(self):
        self.couchserver = couchdb.Server("http://couchdb.telecomnancy.univ-lorraine.fr/")
        self.dbname = 'orphadatabase'
        self.db = self.couchserver[self.dbname]


    def parseOrpha(self):
        for elem in self.db.view("clinicalsigns/GetDiseaseByClignicalSign"):
            value = elem.value
            clinicalSign = value["clinicalSign"]
            clinicalSignName = clinicalSign["Name"]["text"]
            disease = value["disease"]
            diseaseName = disease["Name"]["text"]
            if clinicalSignName in self.orphadataDict :
                self.orphadataDict[clinicalSignName].append(diseaseName)  
            else :
                self.orphadataDict[clinicalSignName] = [diseaseName]
                self.syndromes.append(clinicalSignName)


            def searchDiseaseOrphadata(self,syndrome) :
                if(syndrome in self.orphadataDict):
                    return self.orphadataDict[syndrome]
                else :
                    return []
                    
           
       
        



    s = OrphaDataManager()
    syndrome = "Abnormal colour of the urine/cholic/dark urines"
    disease = s.searchDiseaseOrphadata(syndrome)
    print(disease)
    print("-------------------")
    liste = list()
    for elmt in mydb.view("clinicalsigns/GetDiseaseByClinicalSign") :
        value = elmt.value
        clinicalSign = value["clinicalSign"]
        clinicalSignName = clinicalSign["Name"]["text"]
        if clinicalSignName == syndrome :
            disease = value["disease"]
            diseaseName = disease["Name"]["text"]
            liste.append(diseaseName)
    print(liste)
    print(len(liste))
    print()
    print(len(s.syndromes))
    totalElements = 0
    for syndrome in s.syndromes :
        totalElements += len(s.searchDiseaseOrphadata(syndrome))
    print("Total element {}".format(totalElements))
        

