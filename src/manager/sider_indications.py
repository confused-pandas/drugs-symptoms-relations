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
        data_indications={}
        connexion = pymysql.connect(self.server,self.userName,self.password,self.database)
        try:
            with connexion.cursor() as cursor:
                cursor.execute('SELECT stitch_compound_id,concept_name FROM meddra_all_indications WHERE concept_name LIKE "%'+str(self.clinicalSign)+'%" OR meddra_concept_name LIKE "%'+str(self.clinicalSign)+'%";')
                data_indications[str(self.clinicalSign)]=cursor.fetchall()
        finally: 
            connexion.close()
            return data_indications
        #print(cursor.fetchall())


manager = SiderIndicationsManager("Failure to Thrive")
manager.extractData()
