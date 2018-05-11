from manager.hpo import HpoManager
from manager.omim_onto import OmimOntoManager
from manager.omim_text import OmimTextManager

class DiseaseMapping:

    def __init__(self, clignical_sign):
        self.clignical_sign = clignical_sign
        self.data_omim_text = OmimTextManager(clignical_sign).extractDataFromCs()
        #self.data_hpo = HpoManager(clignical_sign).extractData()

    
    def mapping(self):            
        for key in self.data_omim_text.keys():
            print("Name of the diseases : " + self.data_omim_text[str(key)])
            #data_omim_csv = OmimOntoManager(key).extractData()
            #cui = data_omim_csv[str(key)]
            #for k in data_hpo.keys():
                #omim = OmimOntoManager(k).extractDataFromCui()[k]
                #name = OmimTextManager(omim).extractDataFromOmim()[omim]
                #print("Name of the diseases : "+ name)

    
print(DiseaseMapping("Normocephaly").mapping())
