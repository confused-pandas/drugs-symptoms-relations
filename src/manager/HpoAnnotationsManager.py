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
        cur.execute('SELECT disease_db, sign_id FROM phenotype_annotation WHERE disease_id = '+str(self.diseaseId)+';')
        data_hpo[str(self.diseaseId)] = cur.fetchall()
        print(data_hpo)

manager = HpoAnnotationsManager(42)
manager.extractData()    


"
"""C:\\Users\\mlysr\\Desktop\\GMD\\gmd-project\\res\\database\\hpo\\hpo_annotations.sqlite"""