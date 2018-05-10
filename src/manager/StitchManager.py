import csv
import sys

class StitchManager:
    """Class that enables to get data from Sider DataBase, from the meddra_all_indications table. Has attributes:
    - clinicalSign to look for
    - several attributes necessary for the connection to the databse
    """

    def __init__(self, stitchId):
        self.stitchId = stitchId

  
    def extractData(self):
        f = open("C:\\Users\\mlysr\\Desktop\\GMD\\gmd-project\\res\\database\\stitch\\chemical.sources.tsv",'rb')
        reader = csv.reader(f, delimiter='\t')  
        cpt=0
        data_sti = {}
        
        for ligne in reader:
            cpt+=1
            if cpt>10:
                if ligne[2]=='ATC' and ligne[0]==self.stitchId :
                    data_sti[str(self.stitchId)] = [ligne[3]]
                    print(data_sti)
        f.close()
 

manager = StitchManager("CIDm00452550")
manager.extractData()


"""exemple sticht_coumpound_id pour tester :
    CIDm00452550
    CIDm00452550
    CIDm09804938"""
    
"""path ML : C:\\Users\\mlysr\\Desktop\\GMD\\gmd-project\\res\\database\\stitch\\chemical.sources.tsv"""
