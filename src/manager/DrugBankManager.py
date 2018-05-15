import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser

class DrugBankManager:
    """"DrugBankManager extracts the name of a disease, the synonyms and the umls from the hp.obo file
    """
    def __init__(self, clinicalSign):
        self.clinicalSign = clinicalSign
        self.file = open('../../res/database/drugbank/drugbank.xml')
        self.path_index = "../../res/database/drugbank/index_drugbank"
        self.schema = Schema(drugbank_id=TEXT(stored=True), name=TEXT(stored=True), indication=TEXT(stored=True), toxicity=TEXT(stored=True))


# Create the index
    def index_initialisation(self):
        if not os.path.exists(self.path_index):
            os.mkdir(self.path_index)
        ix = create_in(self.path_index, self.schema)
        ix = open_dir(self.path_index)
        writer = ix.writer()
        return ix, writer

# Extract data from hp.obo and store it in a dictionnary
    def extractData(self, ix, writer):
        data_drugbank = {}
        file = self.file
        line = file.readline()
        while line != "":
            if(line[:4].startswith("<drug")):
                while line[:4].startswith("</drug>")==False:
                    if line[:28].startswith("<drugbank-id primary=\"true\">"):
                        drugbank_id = line[28:]
                        drugbank_id.replace("</drugbank-id>\n","")
                    if line[:6].startswith("<name>"):
                        name = line[6:]
                        name.replace("</name>\n","")
                    if line[:12].startswith("<indication>"):
                        indication = line[12:]
                        indication.replace("</indication>\n","")
                    if line[:10].startswith("<toxicity>"):
                        toxicity = line[10:]
                        toxicity.replace("</toxicity>\n","")
                        writer.add_document(drugbank_id=drugbank_id, name=name, indication=indication, toxicity=toxicity)
                    line = file.readline()
            else:
                line = file.readline()
        writer.commit()
        r = self.parserQuery()
        '''for elem in r:
            data_drugbank[elem.get("drugbank-id")[:-1]] = elem.get("name")[:-21], elem.get("name")[:-1], elem.get("is_a")[:7]'''
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

