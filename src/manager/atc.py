import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser

class AtcManager:

    def __init__(self, atc):
        self.atc = atc
        # en etant dans le dossier src
        self.file = open('../res/database/atc/br08303.keg')
        #self.path = '../res/database/atc/br08303.keg'
        self.path_index = '../res/database/atc/index_atc'
        self.schema = Schema(atc_id=TEXT(stored=True), label=TEXT(stored=True))
        if not os.path.exists(self.path_index):
            os.mkdir(self.path_index)
        self.ix = create_in(self.path_index, self.schema)
        self.ix = open_dir(self.path_index)
    
    def index_initialisation(self):
        
        writer = self.ix.writer()
        file = self.file
        for i in range(0,9):
            line = file.readline() #the 9 first lines are useless
        while line != "":
            atc_id = line[1:].lstrip().split(' ', 1)[0]
            if len(line[1:].lstrip().split(' ', 1)) == 2:
                label = line[1:].lstrip().split(' ', 1)[1].replace('\n', '')
            else:
                label = u"None"
            if atc_id == '':
                atc_id = u"None"
            writer.add_document(atc_id=atc_id, label=label) 
            line = file.readline()
        writer.commit()


    def extractDataFromAtc(self):
        data_atc = {}
        r = parserQuery(self, self.atc, "atc_id")
        for elem in r:
            data_atc[self.atc] = elem.get("label")[1:]
        return data_atc



def parserQuery(self, item, schema_item):
    searcher = self.ix.searcher()
    query = QueryParser(schema_item, self.ix.schema).parse(item)
    results = searcher.search(query)
    return results


manager = AtcManager("D01474")
manager.index_initialisation()
manager.extractDataFromAtc()
