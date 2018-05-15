from manager import *
from causing_drug_mapping import CausingDrugMapping
from curing_drug_mapping import CuringDrugMapping
from disease_mapping import DiseaseMapping
class Main:
    def __init__(self, clignical_sign):
        self.clignical_sign = clignical_sign

    if __name__== '__main__':
        while(True):
            print("Please enter a clinical sign :")
            clinicalSign = input()
            diseases = DiseaseMapping(clinicalSign).mapping()
            if(diseases.count != 0):
                print("//////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
                print("You may have one of those diseases :")
                for disease in diseases:
                    print("- " + disease)
            
            causingDrugs = CausingDrugMapping(clinicalSign).mapping()
            if(causingDrugs.count != 0):
                print("//////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
                print("This may be a side effect to one of those drugs :")
                for drug in causingDrugs:
                    print("- " + drug)

                curingDrugs = CuringDrugMapping(clinicalSign).mapping()
                if(curingDrugs.count != 0):
                    print("//////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
                    print("You may cure these diseases with those drugs :")
                    for curingDrug in curingDrugs:
                        print("- " + curingDrug)
            
            

            