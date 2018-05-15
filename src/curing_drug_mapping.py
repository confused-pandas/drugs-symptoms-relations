from manager.DrugBankManager import DrugBankManager
from manager.sider_indications import SiderIndicationsManager
from manager.stitch import StitchManager
from manager.atc import AtcManager
from pymysql import cursors
import sys

class CuringDrugMapping:
    
    def __init__(self, clinical_sign):
        self.clinical_sign = clinical_sign
        
    def mapping(self):

        #sider import
        data_sider_indic=SiderIndicationsManager(self.clinical_sign).extractData()
        tabCID=[]
        for i in range(0, len(data_sider_indic[self.clinical_sign])):
            tabCID.append(data_sider_indic[self.clinical_sign][i][0])
            
        #remove sider duplicates
        tabCIDunique=[]
        tabCIDunique=(list(set(tabCID))) 
        
        #remove not needed info
        for i in range(0, len(tabCIDunique)):
            tabCIDunique[i]=tabCIDunique[i][4:]

        #stitch import
        data_stitch={}
        for i in range(0, len(tabCIDunique)):
            data_stitch[str(tabCIDunique[i])]=StitchManager(str(tabCIDunique[i])).extractDataFromStitchId()
        
        #print(data_stitch)
        
        #remove duplicates
        data_ATC=[]
        for i in range (0, len(data_stitch)):
            if any(data_stitch[str(tabCIDunique[i])]):
                data_ATC.append(data_stitch[str(tabCIDunique[i])][str(tabCIDunique[i])])
        data_ATC_unique=(list(set(data_ATC)))
        #print(data_ATC_unique)

        #import ATC
        data_drugname=[]
        for atc in data_ATC_unique:
            data_drugname.append(AtcManager(str(atc)).extractDataFromAtc())
        #print(data_drugname)

        #get the name of the drugs (into a list)
        drugname=[]
        for elm in data_drugname:
            if any(elm):
                drugname.append(elm['atc_id'])
            

        #drugbank import
        (data_drugbank_indication, data_drugbank_toxicity) = DrugBankManager(self.clinical_sign).extractData()
        for curingDrug in data_drugbank_indication:
            drugname.append(curingDrug+"DB")

        #print(drugname)
        return drugname
       
            
        

#CausingDrugMapping("failure to thrive").mapping()
            
        
