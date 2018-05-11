import sqlite3
from sqlite3 import Error

class HpoAnnotationsManager:

    def __init__(self, diseaseId):
        self.diseaseId = diseaseId
        self.path = "./res/database/hpo/hpo_annotations.sqlite"

    def extractData(self):
        data_hpo = {}
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        cur.execute('SELECT disease_db FROM phenotype_annotation WHERE disease_id = '+str(self.diseaseId)+' AND disease_db IN ("OMIM", "ORPHA") ;')
        data_hpo[str(self.diseaseId)] = cur.fetchall()
        return data_hpo

manager = HpoAnnotationsManager(1745)
print(manager.extractData())    


"""C:\\Users\\mlysr\\Desktop\\GMD\\gmd-project\\res\\database\\hpo\\hpo_annotations.sqlite"""