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
        param = "%"+ self.clinicalSign +"%"
        try:
            with connection.cursor() as cursor:
                sql = "SELECT stitch_compound_id1, stitch_compound_id2, cui, meddra_concept_type, cui_of_meddra_term FROM meddra_all_indications WHERE side_effect_name="+str(self.clinicalSign)+";"
                cursor.execute(sql)
                data_SE[str(self.clinicalSign)] = cursor.fetchall()
                print(data_SE)
        finally:
            connection.close()
       
manager = SiderSEManager(testClinicalSign) 
manager.extractData()


    
    
    
    
