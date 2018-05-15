from manager.DrugBankManager import DrugBankManager
from manager.sider_se import SiderSEManager
from manager.stitch import StitchManager
from manager.atc import AtcManager
from pymysql import cursors
import sys

class CausingDrugMapping:
    
    def __init__(self, side_effect):
        self.side_effect = side_effect
        
    def mapping(self):

        #sider import
        data_sider_se=SiderSEManager(self.side_effect).extractData()
        tabCID=[]
        for i in range(0, len(data_sider_se[self.side_effect])):
            tabCID.append(data_sider_se[self.side_effect][i]["stitch_compound_id2"])
        
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
        (data_drugbank_indication, data_drugbank_toxicity) = DrugBankManager(self.side_effect).extractData()
        for causingDrug in data_drugbank_toxicity:
            drugname.append(causingDrug)

        print(drugname)
        return drugname
       
            
        

CausingDrugMapping("Acute abdomen").mapping()
            
        
