import biblib

# open file as filedb in read only mode
fileDb = biblib.FileBibDB('bibtex.bib', mode='r')

# open file as db read/write mode,
# no LaTeX encoding of unicode character
newFileDb = biblib.FileBibDB('new.bib', encode=False)

# add fileDb entries to newFileDb
newFileDb.merge_bibdb(fileDb)

# access an entry object refered by its cite-key
entry = newFileDb['JCP-127-234509']
entry.get_tag('year')

# init doi db
doiDb = biblib.DoiBibDB()

# retrieve bibliographic meta data by DOI
entry = doiDb['10.1088/0959-5309/43/5/301']

# add new entries to database
newFileDb.add_entry(entry)
# or this way to set a specific cite-key
# newFileDb['MY_CITE_KEY'] = entry1