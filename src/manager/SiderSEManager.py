import pymysql.cursors

class SiderSEManager:
    
    def __init__(self, clinicalSign):
        self.clinicalSign = clinicalSign
        self.server = "neptune.telecomnancy.univ-lorraine.fr"
        self.database = "gmd"
        self.userName = "gmd-read"
        self.password = "esial"

    def extractData(self):
        connection = pymysql.connect(self.server,self.userName,self.password,self.database, cursorclass=pymysql.cursors.DictCursor)
        param = "%"+ self.clinicalSign +"%"
        try:
            with connection.cursor() as cursor:
                sql = "SELECT stitch_compound_id1, stitch_compound_id2, cui, meddra_concept_type, cui_of_meddra_term, side_effect_name FROM meddra_all_indications"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
        finally:
            connection.close()
       
manager = SiderSEManager()




    
    
    
    
