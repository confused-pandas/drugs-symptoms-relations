import sqlite3
from sqlite3 import Error

class HpoAnnotationsManager:

    def __init__(self, hpId):
        self.hpId = hpId
        self.path = "../res/database/hpo/hpo_annotations.sqlite"

    def extractData(self):
        data_hpo = {}
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute('SELECT disease_id, disease_db FROM phenotype_annotation WHERE sign_id = "'+str(self.hpId)+'";')
        data_hpo[str(self.hpId)] = cur.fetchall()
        return data_hpo

#manager = HpoAnnotationsManager('HP:0003593')
#l=manager.extractData()
#print(l)   


"""C:\\Users\\mlysr\\Desktop\\GMD\\gmd-project\\res\\database\\hpo\\hpo_annotations.sqlite"""