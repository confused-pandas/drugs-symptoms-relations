from manager.hpo import HpoManager
from manager.hpo_annotations import HpoAnnotationsManager
from manager.omim_onto import OmimOntoManager
from manager.omim_text import OmimTextManager

class DiseaseMapping:

    def __init__(self, clignical_sign):
        self.clignical_sign = clignical_sign
        #self.data_hpo = HpoManager(clignical_sign).extractData()

    
    def mapping(self):
        data_omim_text = OmimTextManager(self.clignical_sign).extractDataFromCs()
        data_hpo = HpoManager(self.clignical_sign).extractDataFromSynonym()
        
        # Search in the synonyms
        for cui in data_hpo.keys():
            list_omim = []
            #list_orpha = []
            # First we extract the OMIM
            hp_id = "HP:"+ data_hpo[cui][1]
            l = HpoAnnotationsManager(hp_id).extractData()
            for i in range(0, len(l[hp_id])):
                if l[hp_id][i][1] == "OMIM":
                    list_omim.append(l[hp_id][i][0])
                #if l[i][2] == "ORPHA":
                    #list_orpha.append()
            for omim in list_omim:
                if OmimTextManager(omim).extractDataFromOmim() == {}:
                    print("pas de référence pour cet id")
                else:
                    disease_name = OmimTextManager(omim).extractDataFromOmim()[omim]
                    print(disease_name)
                    print("------------------------------")

        # Search in omim
        for key in data_omim_text.keys():
            disease_name = data_omim_text[str(key)]
            print(disease_name)
            print("-------------------")
            
        
    
DiseaseMapping("Abnormality").mapping()
