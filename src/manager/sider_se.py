import pymysql.cursors

class SiderSEManager:
    
    def __init__(self, clinicalSign):
        self.clinicalSign = clinicalSign
        self.server = "neptune.telecomnancy.univ-lorraine.fr"
        self.database = "gmd"
        self.userName = "gmd-read"
        self.password = "esial"

    def extractData(self):
        data_SE={}
        connection = pymysql.connect(self.server,self.userName,self.password,self.database, cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT stitch_compound_id1, stitch_compound_id2, cui, meddra_concept_type, cui_of_meddra_term FROM meddra_all_se WHERE side_effect_name LIKE "%'+str(self.clinicalSign)+'%";')
                #cmd="SELECT stitch_compound_id1, stitch_compound_id2, cui, meddra_concept_type, cui_of_meddra_term FROM meddra_all_se WHERE side_effect_name LIKE %%%s%;"%(str(self.clinicalSign))
                #cursor.execute(cmd)
                data_SE[str(self.clinicalSign)] = cursor.fetchall()
        finally:
            connection.close()
            return data_SE
       
manager = SiderSEManager("Acut") 
manager.extractData()
print(manager.extractData())    



