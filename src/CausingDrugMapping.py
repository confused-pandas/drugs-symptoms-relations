from manager.sider_se import SiderSEManager
from manager.stitch import StitchManager
from manager.atc import AtcManager
import sys

class CausingDrugMapping:
    
    def __init__(self, side_effect):
        self.side_effect = side_effect
        
    def mapping(self):
        #on récupère le CID correspondant au Side effect
        data_sider_se=SiderSEManager(self.side_effect).extractData()
        tabCID=[]
        for i in range(0, len(data_sider_se[self.side_effect])):
            tabCID.append(data_sider_se[self.side_effect][i]["stitch_compound_id2"])
        
        tabCIDunique=[]
        tabCIDunique=(list(set(tabCID))) #•on élimine les doublons
        
        for i in range(0, len(tabCIDunique)):
            tabCIDunique[i]=tabCIDunique[i][3:] #on enlève les lettres CID
        
        data_stitch={}
        for i in range(0, len(tabCIDunique)):
            data_stitch[tabCIDunique[i]]=StitchManager(tabCIDunique[i])
            
        
