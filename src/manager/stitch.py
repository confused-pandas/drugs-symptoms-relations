import csv
import sys
import os, os.path
from whoosh.index import *
from whoosh.fields import *
from whoosh.qparser import QueryParser

class StitchManager:
    """Class that enables to get data from Sider DataBase, from the meddra_all_indications table. Has attributes:
    - clinicalSign to look for
    - several attributes necessary for the connection to the databse
    """

    def __init__(self, stitchId):
        self.stitchId = stitchId
        self.path = '../res/database/stitch/chemical.sources.tsv'
        self.path_index = '../res/database/stitch/index_stitch'
        self.schema = Schema(stitch_id=TEXT(stored=True), atc=TEXT(stored=True))
  
    
    def index_initialisation(self):
        if not os.path.exists(self.path_index):
            os.mkdir(self.path_index)
        ix = create_in(self.path_index, self.schema)
        ix = open_dir(self.path_index)
        writer = ix.writer()
        f = open(self.path,'r')
        reader = csv.reader(f, delimiter='\t')
        cpt=0
        for ligne in reader:
            cpt+=1
            if cpt>10 and cpt<10000:
                stitch_id = ligne[0][4:]
                if ligne[2]=='ATC':
                    atc = ligne[3]
                else: 
                    atc = u"None"
                    break
            else:
                atc = u"None"
                stitch_id = u"None"
            if cpt > 10000:
                break
            #print("stich_id :" , stitch_id, " atc :", atc)
            writer.add_document(stitch_id=stitch_id, atc=atc)
        f.close()
        writer.commit()


    def extractDataFromStitchId(self):
        data_stitch = {}
        r = parserQuery(self, self.path_index, self.stitchId, "stitch_id")
        for elem in r:
            data_stitch[elem.get("stitch_id")] = elem.get("atc")
        return data_stitch
        


def parserQuery(self, path, item, schema_item):
    ix = open_dir(path)
    searcher = ix.searcher()
    query = QueryParser(schema_item, ix.schema).parse(item)
    results = searcher.search(query)
    return results
 

#manager = StitchManager("00004205")
#manager.index_initialisation()
#print(manager.extractDataFromStitchId())

"""exemple sticht_coumpound_id pour tester :
    CIDm00452550
    CIDm00452550
    CIDm09804938"""
    
"""path ML : C:\\Users\\mlysr\\Desktop\\GMD\\gmd-project\\res\\database\\stitch\\chemical.sources.tsv"""
