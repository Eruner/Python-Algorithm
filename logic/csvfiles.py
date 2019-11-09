import csv

def loadCsv(fileName, scvHeader):
	print(fileName)
	print(scvHeader)
	raw_data = open(fileName, 'rt')
	reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
	items = list(reader)
	raw_data.close()
	return items

def writeCsv(fileName, header, items):
	csvfile = open(fileName, 'wt')
	writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_NONE, quotechar='', escapechar='\n',lineterminator='\n')
	writer.writerow(header)
	writer.writerows(items)
	csvfile.close()