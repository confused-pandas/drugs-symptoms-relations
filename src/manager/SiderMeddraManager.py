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
        connection = pymysql.connect(self.server,self.userName,self.password,self.database, cursorclass=pymysql.cursors.DictCursor)
        param = "%"+ self.clinicalSign +"%"
        try:
            with connection.cursor() as cursor:
                sql = "SELECT cui, label FROM meddra_all_indications"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
        finally:
            connection.close()
       
manager = SiderMeddraManager()


    
