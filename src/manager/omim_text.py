import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser

class OmimTextManager:
    """"OmimTextManager extract the Omim, the Clignical Signs and the name of a disease 
        from the Omim.txt file
    """

    def __init__(self, item):
        self.item = item
        self.file = open('./res/database/omim/omim.txt')
        self.path_index = "./res/database/omim/index_omim"
        self.schema = Schema(omim_id=TEXT(stored=True), cs=TEXT(stored=True), title=TEXT(stored=True))

    # Create the index
    def index_initialisation(self):
        if not os.path.exists(self.path_index):
            os.mkdir(self.path_index)
        ix = create_in(self.path_index, self.schema)
        ix = open_dir(self.path_index)
        writer = ix.writer()
        file = self.file
        line = file.readline()
        while line != "":
            if line == "*FIELD* NO\n":
                id = file.readline()
                id = id.replace("\n","")
            if line == "*FIELD* TI\n":
                line = file.readline()
                titre = ""
                while not line.startswith("*"):
                    titre = titre+line
                    titre = titre.replace("\n","")
                    line = file.readline()
            if line == "*FIELD* CS\n":
                line = file.readline()
                clign = ""
                while not line.startswith("*"):
                    clign = clign + line
                    clign = clign.replace("\n","")
                    line = file.readline()
                writer.add_document(omim_id=id, cs=clign, title=titre)
            line = file.readline()
        writer.commit()
        
    # Extract data from Omim.txt and store it in a dictionnary
    def extractDataFromCs(self):
        data_omimt = {}                   
        r = parserQuery(self, self.item, "cs")
        for elem in r:
            data_omimt[elem.get("omim_id")] = elem.get("title")[7:].lstrip()
        return data_omimt

    def extractDataFromOmim(self):
        data_omimt = {}
        r = parserQuery(self, self.item, "omim_id")
        for elem in r:
            data_omimt[self.item] = elem.get("title")[7:].lstrip()
        return data_omimt



def parserQuery(self, item, schema_item):
    ix = open_dir(self.path_index)
    searcher = ix.searcher()
    query = QueryParser(schema_item, ix.schema).parse(item)
    results = searcher.search(query)
    results[0]
    return results



manager = OmimTextManager("Normocephaly")
#manager.index_initialisation()
print(manager.extractDataFromCs())