from lxml import etree


context = etree.iterparse('./res/database/drugbank/full_database.xml', events=('end',), tag='Title')


def fast_iter(context, func):
    for event, elem in context:
        func(elem)
        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]
    del context

def func():
    for event, elem in context:
        out.write('%s\n' % elem.text.encode('utf-8'))        
    
        # It's safe to call clear() here because no descendants will be accessed
        elem.clear()
    
        # Also eliminate now-empty references from the root node to <Title> 
        while elem.getprevious() is not None:
            del elem.getparent()[0]

fast_iter(context, func())