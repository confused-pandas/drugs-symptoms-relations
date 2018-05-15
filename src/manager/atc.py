import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser

class AtcManager:

    def __init__(self, atc):
        self.atc = atc
        self.file = open('./res/database/atc/br08303.keg')
        self.path = './res/database/atc/br08303.keg'
        self.path_index = './res/database/atc/index_atc'
        self.schema = Schema(atc_id=TEXT(stored=True), label=TEXT(stored=True))

    
    def index_initialisation(self):
        if not os.path.exists(self.path_index):
            os.mkdir(self.path_index)
        ix = create_in(self.path_index, self.schema)
        ix = open_dir(self.path_index)
        writer = ix.writer()
        file = self.file
        for i in range(0,9):
            line = file.readline()
        while line != "":
            atc_id = unicode(line[1:].lstrip().split(' ', 1)[0])
            if len(line[1:].lstrip().split(' ', 1)) == 2:
                label = unicode(line[1:].lstrip().split(' ', 1)[1].replace('\n', ''))
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
            data_atc["atc_id"] = elem.get("label")[1:]
        return data_atc



def parserQuery(self, item, schema_item):
    ix = open_dir(self.path_index)
    searcher = ix.searcher()
    query = QueryParser(schema_item, ix.schema).parse(item)
    results = searcher.search(query)
    return results


#manager = AtcManager("D01474")
#manager.index_initialisation()
#manager.extractDataFromAtc()
