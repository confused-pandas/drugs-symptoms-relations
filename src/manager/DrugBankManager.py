import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser

class DrugBankManager:
    """"DrugBankManager extracts the name of a disease, the synonyms and the umls from the hp.obo file
    """
    def __init__(self, clinicalSign):
        self.clinicalSign = clinicalSign
        self.file = open('./res/database/drugbank/drugbank.xml')
        self.path = './res/database/drugbank/drugbank.xml'
        self.path_index = './res/database/drugbank/drugbank_index'
        self.schema = Schema(name=TEXT(stored=True), indication=TEXT(stored=True), toxicity=TEXT(stored=True))


# Create the index
    def index_initialisation(self):
        if not os.path.exists(self.path_index):
            os.mkdir(self.path_index)
        ix = create_in(self.path_index, self.schema)
        ix = open_dir(self.path_index)
        writer = ix.writer()
        file = self.file
        line = file.readline()
        print(line)
        nameSaved = False
        toxicitySaved = False
        indicationSaved = False
        print(line)
        while not line.startswith("</drugbank>"):
            if(line.startswith("<drug type=")):
                #drugbank_id="null"
                name="null"
                indication="null"
                toxicity="null"
                line = file.readline()
                #print(line)
                while not line.startswith("</drug>"):
                    line.lstrip()
                    #if line.startswith("<drugbank-id primary="):
                        #drugbank_id = line[28:]
                        #drugbank_id.replace("</drugbank-id>\n","")
                        #print(line)
                    if line.startswith("  <name>")  and not nameSaved:
                        name = line[8:]
                        name = name[:-8]
                        nameSaved = True
                        print("name = " + name)
                    if line.startswith("  <indication>") and not indicationSaved:
                        indication = line[14:]
                        indication = indication[:-14]
                        indicationSaved = True
                        print("indication = " + indication)
                    if line.startswith("  <toxicity>") and not toxicitySaved:
                        toxicity = line[12:]
                        toxicity = toxicity[:-12]
                        toxicitySaved = True
                        print("toxicity = " + toxicity)
                    line = file.readline()
                if(not name.startswith("null") and not indication.startswith("null") and not toxicity.startswith("null")):
                    print("name = " + name + " indication = " +  indication + " toxicity = " + toxicity)
                    writer.add_document(name=name, indication=indication, toxicity=toxicity)
            else:
                line = file.readline()
        writer.commit()
        print("end")

# Extract data from hp.obo and store it in a dictionnary
    def extractData(self):
        data_indication_drugbank = []
        data_toxicity_drugbank = []
        (r1,r2) = self.parserQuery()
        for elem in r1:
            data_indication_drugbank.append(elem.get("name"))
        for elem in r2:
            data_toxicity_drugbank.append(elem.get("name"))
        return (data_indication_drugbank,data_toxicity_drugbank)

    def parserQuery(self):
        ix = open_dir(self.path_index)
        searcher = ix.searcher()
        #print(self.clinicalSign)
        indicationQuery = QueryParser("indication", ix.schema).parse(self.clinicalSign)
        toxicityQuery = QueryParser("toxicity", ix.schema).parse(self.clinicalSign)
        indicationResults = searcher.search(indicationQuery)
        toxicityResults = searcher.search(toxicityQuery)
        #print("indication len = " + str(len(indicationResults)))
        #print(searcher.search(nameQuery)[0])
        #print(indicationResults)
        return (indicationResults, toxicityResults)

#manager = DrugBankManager("thrombocytopenia")

#manager.extractData()
#manager = DrugBankManager("overdose")
#manager.index_initialisation()
#print(manager.extractData())



