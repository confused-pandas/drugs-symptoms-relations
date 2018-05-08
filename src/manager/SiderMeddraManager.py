# -*- coding: utf-8 -*-
"""
Created on Tue May 08 14:52:36 2018

@author: mlysr
"""
import pymysql.cursors

class SiderMeddraManager:
    
    def __init__(self, clinicalSign):
        self.clinicalSign = clinicalSign
        self.server = "neptune.telecomnancy.univ-lorraine.fr"
        self.database = "gmd"
        self.userName = "gmd-read"
        self.password = "esial"

    def extractData(self):
        data_meddra={}
        connection = pymysql.connect(self.server,self.userName,self.password,self.database, cursorclass=pymysql.cursors.DictCursor)
        param = "%"+ self.clinicalSign +"%"
        try:
            with connection.cursor() as cursor:
                sql = "SELECT cui FROM meddra_all_indications WHERE label="+str(self.clinicalSign)+";"
                cursor.execute(sql)
                data_meddra[str(self.clinicalSign)] = cursor.fetchall()
                print(data_meddra)
        finally:
            connection.close()
       
manager = SiderMeddraManager(testClinicalSign) 
manager.extractData()


    
