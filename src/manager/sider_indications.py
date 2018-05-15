import pymysql

class SiderIndicationsManager:
    """Class that enables to get data from Sider DataBase, from the meddra_all_indications table. Has attributes:
    - clinicalSign to look for
    - several attributes necessary for the connection to the databse
    """

    def __init__(self, clinicalSign):
        self.clinicalSign = clinicalSign
        self.server = "neptune.telecomnancy.univ-lorraine.fr"
        self.database = "gmd"
        self.userName = "gmd-read"
        self.password = "esial"

    def extractData(self):
        connexion = pymysql.connect(self.server,self.userName,self.password,self.database)
        cursor = connexion.cursor()
        cursor.execute('SELECT stitch_compound_id, cui, concept_name,cui_of_meddra_term,meddra_concept_name FROM meddra_all_indications WHERE concept_name LIKE "%'+str(self.clinicalSign)+'%" OR meddra_concept_name LIKE "%'+str(self.clinicalSign)+'%";')
        print(cursor.fetchall())


manager = SiderIndicationsManager("Hypo")
manager.extractData()
