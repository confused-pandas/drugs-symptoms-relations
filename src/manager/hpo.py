import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser

class HpoManager:
    """"HpoManager extract the name of a disease, the synonyms and the umls + is_a 
        from the hp.obo file
    """

    def __init__(self, synonym):
        self.synonym = synonym
        self.file = open('./res/database/hpo/hp.obo')
        self.path_index = "./res/database/hpo/index_hpo"
        self.path_index_synonym = "./res/database/hpo/index_hpo_synonym"
        self.schema = Schema(name=TEXT(stored=True), synonym=TEXT(stored=True), cui=TEXT(stored=True), is_a=TEXT(stored=True))

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
            if line.startswith("name: "):
                name = line[6:]
                name.replace("\n","")
            if line.startswith('synonym: "'):
                synonym = []
                while line.startswith("synonym"):
                    synonym.append(line[10:].replace('\n',''))
                    line = file.readline()
            if line.startswith("xref: UMLS:"):
                xref = line[11:]
                xref.replace("\n","")
            if line.startswith("is_a: HP:"):
                is_a = []
                while line.startswith("is_a"):
                    is_a.append(line[19:].replace('\n',''))
                    line = file.readline()
                writer.add_document(name=name, synonym=synonym, cui=xref, is_a=is_a)
            line = file.readline()
        writer.commit()

    def index_initialisation_synonym(self):
        if not os.path.exists(self.path_index_synonym):
            os.mkdir(self.path_index_synonym)
        ix = create_in(self.path_index_synonym, self.schema)
        ix = open_dir(self.path_index_synonym)
        writer = ix.writer()
        file = self.file
        line = file.readline()
        while line != "":
            if line.startswith("name: "):
                name = line[6:]
                name.replace("\n","")
            if line.startswith('synonym: "'):
                synonym = ""
                while line.startswith('synonym'):
                    synonym = synonym + " " + line[10:].replace('\n','')[:line[10:].index('"')]
                    line = file.readline()
            if line.startswith("xref: UMLS:"):
                xref = line[11:]
                xref.replace("\n","")
            if line.startswith("is_a: HP:"):
                is_a = []
                while line.startswith("is_a"):
                    is_a.append(line[19:].replace('\n',''))
                    line = file.readline()
                writer.add_document(name=name, synonym=synonym, cui=xref, is_a=is_a)
            line = file.readline()
        writer.commit()
        
    # Extract data from hp.obo and store it in a dictionnary
    def extractData(self):
        data_hpo = {}
        r = parserQuery(self, self.path_index, self.synonym, "name")
        for elem in r:
            l = []
            for i in range(0, len(elem.get("synonym"))):
                l.append(elem.get("synonym")[i][:elem.get("synonym")[i].index('"')])
            data_hpo[elem.get("cui")[:-1]] = l #, elem.get("name")[:-1] #, elem.get("is_a")
        return data_hpo

    def extractDataFromSynonym(self):
        data_hpo = {}
        r = parserQuery(self, self.path_index_synonym, self.synonym, "synonym")
        for elem in r:
            data_hpo[elem.get("cui")[:-1]] = elem.get("name")[:-1]
        return data_hpo


def parserQuery(self, path, item, schema_item):
    ix = open_dir(path)
    searcher = ix.searcher()
    query = QueryParser(schema_item, ix.schema).parse(item)
    results = searcher.search(query)
    results[0]
    return results

manager = HpoManager("Abnormality")
#manager.index_initialisation()
#manager.index_initialisation_synonym()
print(manager.extractDataFromSynonym())

# Abnormality of craniofacial shape