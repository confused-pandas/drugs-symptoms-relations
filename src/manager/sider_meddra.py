# -*- coding: utf-8 -*-
"""
Created on Tue May 08 14:52:36 2018

@author: mlysr
"""
import pymysql

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
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT cui FROM meddra WHERE label=%s;',str(self.clinicalSign))
                data_meddra[str(self.clinicalSign)] = cursor.fetchall()
                print(data_meddra)
        finally:
            connection.close()
       
#manager = SiderMeddraManager("Acute abdomen") 
#manager.extractData()


    
