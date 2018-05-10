import os, os.path
from whoosh import index as ind
from whoosh.fields import *
import codecs
clinicalSign = u"thrombocytopenia" #for the example
filePath=u"/Users/AnissaBokhamy/Documents/Cours/2A/Semestre4/GMD/Projet/gmd-project/res/database/drugbank/drugbank.xml"
#schema necessary to know what type of info will be treated
schema = Schema(title=TEXT(stored=True),content=TEXT)
if not os.path.exists("drugbank_index"):
    os.mkdir("drugbank_index") #creates a storage object to contain the index
ix = ind.create_in("drugbank_index",schema) #creating an index in the dir index with the use of the schema
ix = ind.open_dir("drugbank_index") #opening the index in order to use it
writer = ix.writer() #creating an IndexWriter object that enables adding documents to the index
with codecs.open(filePath, "r","utf-8") as f:
    content = f.read()
    f.close()
    writer.add_document(title=filePath, content=content)
writer.commit() #saves the documents into the index

from whoosh.qparser import QueryParser
query = QueryParser("<indication>",ix.schema)
queryResult = query.parse(clinicalSign)
with ix.searcher() as searcher:
    results = searcher.search(queryResult)
print(results[0])
