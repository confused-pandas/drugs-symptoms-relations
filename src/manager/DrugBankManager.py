import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser

class DrugBankManager:
    """"DrugBankManager extracts the name of a disease, the synonyms and the umls from the hp.obo file
    """
    def __init__(self, clinicalSign):
        self.clinicalSign = clinicalSign
        self.file = open('../res/database/drugbank/drugbank.xml')
        self.path_index = "../res/database/drugbank/index_drugbank"
        self.schema = Schema(drugbank_id=TEXT(stored=True), name=TEXT(stored=True), indication=TEXT(stored=True), toxicity=TEXT(stored=True))


# Create the index
    def index_initialisation(self):
        if not os.path.exists(self.path_index):
            os.mkdir(self.path_index)
        ix = create_in(self.path_index, self.schema)
        ix = open_dir(self.path_index)
        writer = ix.writer()
        file = self.file
        line = file.readline()
        nameSaved = False
        print(line)
        while line != "":
            if(line.startswith("<drug type=")):
                line = file.readline()
                print(line)
                while not line.startswith("</drug>"):
                    drugbank_id="null"
                    name="null"
                    indication="null"
                    toxicity="null"
                    line.lstrip()
                    if line.startswith("<drugbank-id primary="):
                        drugbank_id = line[28:]
                        drugbank_id.replace("</drugbank-id>\n","")
                        print(line)
                    if line.startswith("  <name>")  and not nameSaved:
                        name = line[8:]
                        name.lstrip()
                        name.replace("</name>\n","")
                        nameSaved = True
                        print("name = " + name)
                    if line.startswith("  <indication>"):
                        indication = line[14:]
                        indication.lstrip()
                        indication.replace("</indication>","")
                        print("indication = " + indication)
                    if line.startswith("<toxicity>"):
                        toxicity = line[12:]
                        toxicity.lstrip()
                        toxicity.replace("</toxicity>\n","")
                        print("toxicity = " + toxicity)
                    writer.add_document(drugbank_id=drugbank_id, name=name, indication=indication, toxicity=toxicity)
                    line = file.readline()
            else:
                line = file.readline()
        writer.commit()
        return ix, writer

# Extract data from hp.obo and store it in a dictionnary
    def extractData(self, ix, writer):
        data_drugbank = {}
        r = self.parserQuery()
        for elem in r:
            data_drugbank[elem.get("drugbank-id")[:-1]] = elem.get("name")[:-21], elem.get("name")[:-1], elem.get("is_a")[:7]
        print(data_drugbank)

    def parserQuery(self):
        searcher = ix.searcher()
        indicationQuery = QueryParser("indication", ix.schema).parse(self.clinicalSign)
        toxicityQuery = QueryParser("toxicity", ix.schema).parse(self.clinicalSign)
        indicationResults = searcher.search(indicationQuery)
        toxicityResults = searcher.search(toxicityQuery)
        indicationResults[0]
        toxicityResults[0]
        return indicationResults

manager = DrugBankManager("thrombocytopenia")
ix, writer = manager.index_initialisation()
manager.extractData(ix, writer)

