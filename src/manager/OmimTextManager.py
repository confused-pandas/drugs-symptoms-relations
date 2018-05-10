import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser

class OmimTextManager:
    """"OmimTextManager extract the Omim, the Clignical Signs and the name of a disease 
        from the Omim.txt file
    """

    def __init__(self, omim_id):
        self.omim_id = omim_id
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
        return ix, writer
        
    # Extract data from Omim.txt and store it in a dictionnary
    def extractData(self, ix, writer):
        data_omimt = {}
        file = self.file
        line = file.readline()
        b = False
        found = False
        while line != "" and b==False:
            if line == "*FIELD* NO\n":
                id = file.readline()
                id = id.replace("\n","")
                if id == self.omim_id:
                    omim = id
                    found = True
                if omim!=id and found==True:
                    b=True
            if line == "*FIELD* TI\n":
                titre = []
                while line != "*FIELD* TX\n":
                    line = file.readline()    
                    titre.append(line)
                titre.pop()
            if line == "*FIELD* CS\n":
                clign = []
                while line != "*FIELD* CN\n":
                    line = file.readline()
                    clign.append(line)
                clign.pop()
                writer.add_document(omim_id=omim, cs=clign, title=titre)
            line = file.readline()

        writer.commit()
        r = parserQuery(self.omim_id)
        for elem in r:
            data_omimt[self.omim_id] = elem.get("omim_id"), elem.get("title"), elem.get("cs")
        print(data_omimt)



def parserQuery(omim):
    searcher = ix.searcher()
    query = QueryParser("omim_id", ix.schema).parse(omim)
    results = searcher.search(query)
    results[0]
    return results

manager = OmimTextManager("100050")
ix, writer = manager.index_initialisation()
manager.extractData(ix, writer)