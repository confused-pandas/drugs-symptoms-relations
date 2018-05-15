import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser
import csv

class OmimOntoManager:

    def __init__(self, item):
        self.item = item
        self.path = '../res/database/omim/omim_onto.csv'
        self.path_index = '../res/database/omim/index_omim_onto.csv'
        self.schema = Schema(cui=TEXT(stored=True), omim=TEXT(stored=True))

    def index_initialisation(self):
        if not os.path.exists(self.path_index):
            os.mkdir(self.path_index)
        ix = create_in(self.path_index, self.schema)
        ix = open_dir(self.path_index)
        writer = ix.writer()
        with open(self.path,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                cui = row[5][:8]
                cur = row[0][42:]
                if cur.startswith("MTHU"):
                    omim = row[0][46:52]
                else:
                    omim = row[0][42:48]
                writer.add_document(cui=cui, omim=omim)
            writer.commit()

    def extractDataFromCui(self):
        data_omimc = {}
        r = parserQuery(self, self.item, "cui")
        for elem in r:
            data_omimc[self.item] = elem.get("omim")
        return data_omimc



def parserQuery(self, item, schema_item):
    ix = open_dir(self.path_index)
    searcher = ix.searcher()
    query = QueryParser(schema_item, ix.schema).parse(item)
    results = searcher.search(query)
    return results

#manager = OmimOntoManager("C0730362")
#manager.index_initialisation()
#print(manager.extractDataFromCui())