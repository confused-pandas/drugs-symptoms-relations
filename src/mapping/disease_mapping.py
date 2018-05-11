from manager.hpo import HpoManager
from manager.hpo_annotations import HpoAnnotationsManager
from manager.omim_onto import OmimOntoManager
from manager.omim_text import OmimTextManager

class DiseaseMapping:

    def __init__(self, clignical_sign):
        self.clignical_sign = clignical_sign
        self.data_omim_text = OmimTextManager(clignical_sign).extractData()

    
    def mapping(self):
        for key in self.data_omim_text.keys():
            print("Name of the diseases : " + data_omim_text[str(key)])
            data_omim_csv = OmimOntoManager(key).extractData()
            cui = data_omim_csv[str(key)]
