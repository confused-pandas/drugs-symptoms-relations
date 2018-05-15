import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser

class HpoManager:
    """"HpoManager extracts the name of a disease, the synonyms and the umls + is_a 
        from the hp.obo file
    """

    def __init__(self, synonym):
        self.synonym = synonym
        self.file = open('./res/database/hpo/hp.obo')
        self.path_index = "./res/database/hpo/index_hpo"
        self.schema = Schema(name=TEXT(stored=True), synonym=TEXT(stored=True), umls=TEXT(stored=True), is_a=TEXT(stored=True))

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
        data_hpo = {}
        file = self.file
        line = file.readline()
        while line != "":
            if line[:6].startswith("name: "):
                name = line[6:]
                name.replace("\n","")
            if line[:10].startswith('synonym: "'):
                synonym = line[10:]
                synonym.replace("\n","")
            if line[:11].startswith("xref: UMLS:"):
                xref = line[11:]
                xref.replace("\n","")
            if line[:9].startswith("is_a: HP:"):
                is_a = line[9:]
                is_a.replace("\n","")
                writer.add_document(name=name, synonym=synonym, umls=xref, is_a=is_a)
            line = file.readline()

        writer.commit()
        r = self.parserQuery()
        for elem in r:
            data_hpo[elem.get("umls")[:-1]] = elem.get("synonym")[:-21], elem.get("name")[:-1], elem.get("is_a")[:7]
        print(data_hpo)
        return

    def parserQuery(self):
        searcher = ix.searcher()
        query = QueryParser("synonym", ix.schema).parse(self.synonym)
        results = searcher.search(query)
        results[0]
        return results

#manager = HpoManager("Abnormality of body height")
#ix, writer = manager.index_initialisation()
#manager.extractData(ix, writer)