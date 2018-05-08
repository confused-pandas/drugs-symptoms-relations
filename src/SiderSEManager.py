# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:49:41 2018

@author: mlysr
"""
import pymysql.cursors

class SiderSEManager:
    ""
    
    def _init_(self, clinicalSign):
        self.clinicalSign=clinicalSign
        self.host ='neptune.telecomnancy.univ-lorraine.fr'
        self.user ='gmd-read'
        self.password = 'esial'
        self.db= 'gmd'
        
    def extractData(self):
        connexion = pymysql.connect(self.server,self.userName,self.password,self.database)
        cursor = connexion.cursor()
        
    
