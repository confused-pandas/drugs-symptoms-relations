from manager.hpo import HpoManager
from manager.hpo_annotations import HpoAnnotationsManager
from manager.omim_onto import OmimOntoManager
from manager.omim_text import OmimTextManager
from manager.orphadata import OrphaDataManager
import sys

class DiseaseMapping:

    def __init__(self, clignical_sign):
        self.clignical_sign = clignical_sign
        #self.data_hpo = HpoManager(clignical_sign).extractData()

    
    def mapping(self):
        data_omim_text = OmimTextManager(self.clignical_sign).extractDataFromCs()
        data_hpo = HpoManager(self.clignical_sign).extractDataFromSynonym()
        diseaseList = []

        list_orpha = OrphaDataManager(self.clignical_sign).extractNameFromCs()
        for elem in list_orpha:
            print("SOURCE -> ORPHA")
            print("NAME -> | ", elem)
            print("---------------------------------------------------------")

        cpt_not_matched = 0  # Number of element not matched
        cpt_matched = 0   # Number of element matched
        cpt_matched_orpha = 0
        cpt_not_matched_orpha = 0
        # Search in the synonyms
        for cui in data_hpo.keys():
            list_omim = []
            list_orpha = []
            # First we extract the OMIM
            hp_id = "HP:"+ data_hpo[cui][1]
            l = HpoAnnotationsManager(hp_id).extractData()
            for i in range(0, len(l[hp_id])):
                if l[hp_id][i][1] == "OMIM":
                    list_omim.append(l[hp_id][i][0])
                if l[hp_id][i][1] == "ORPHA":
                    list_orpha.append(l[hp_id][i][0])
            for omim in list_omim:
                if OmimTextManager(omim).extractDataFromOmim() == {}:
                   cpt_not_matched += 1 
                else:
                    cpt_matched += 1
                    disease_name = OmimTextManager(omim).extractDataFromOmim()[omim]
                    print("OMIM -> |"+omim+"|"+ "----SOURCE -> |"+"HP.OBO")
                    print("NAME -> |"+disease_name)
                    print("---------------------------------------------------------------")

            
            for orphanb in list_orpha:
                if OrphaDataManager(int(orphanb)).extractNameFromId() == "":
                    cpt_not_matched_orpha += 1
                else:
                    cpt_matched_orpha += 1
                    disease_name = OrphaDataManager(int(orphanb)).extractNameFromId()
                    print("SOURCE -> | HP.OBO ORPHA")
                    print("NAME -> |"+disease_name)
                    print("--------------------------------------------------------------")



        # Search in omim
        for key in data_omim_text.keys():
            disease_name = data_omim_text[str(key)]
            diseaseList.append(disease_name)
            print("OMIM -> |"+key+"|"+ "----SOURCE -> |"+"OMIM.TXT")
            print("NAME -> |"+disease_name)
            print("------------------------------------------------------------------------")

    
        if (cpt_matched+cpt_not_matched == 0):
            q = "No mapping necessary for these data"
            print("Quality of Mapping : ", q)
        else:
            q = cpt_matched/(cpt_matched+cpt_not_matched)*100
            print("Quality of Mapping between omim.txt and hpo_annotations.sqlite : ", q, "%")
        
            
        return diseaseList
    
#DiseaseMapping(sys.argv[1]).mapping()
