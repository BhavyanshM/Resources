import scholarly
# Retrieve the author's data, fill-in, and print

f = open('gs-papers.txt')

for line in f:
	search_query = scholarly.search_pubs_query(line)
	publication = next(search_query)
	print(publication.bib['title'], publication.citedby, publication.bib['year'])



