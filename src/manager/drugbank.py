"""import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser
import xml.etree.ElementTree as ET

class DrugBankManager:

    def __init__(self, item):
        self.item = item
        self.path = './res/database/drugbank/full_database.xml'
        self.path_index = "./res/database/drugbank/index_drug"
        self.schema = Schema(name=TEXT(stored=True), indication=TEXT(stored=True), toxicity=TEXT(stored=True))

    # Create the index
    def index_initialisation(self):
        if not os.path.exists(self.path_index):
            os.mkdir(self.path_index)
        ix = create_in(self.path_index, self.schema)
        ix = open_dir(self.path_index)
        writer = ix.writer()
        tree = ET.parse(self.path)
        root = tree.getroot()
        for child in root:
            print(child)

        writer.commit()
        
    # Extract data from Omim.txt and store it in a dictionnary
    def extractNameFromToxicity(self):
        data_drug = {}                   
        r = parserQuery(self, self.item, "toxicity")
        for elem in r:
            data_drug[elem.get("name")] = elem.get("")[7:].lstrip()
        return data_drug



def parserQuery(self, item, schema_item):
    ix = open_dir(self.path_index)
    searcher = ix.searcher()
    query = QueryParser(schema_item, ix.schema).parse(item)
    results = searcher.search(query)
    return results


