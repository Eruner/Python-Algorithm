import csv

def loadCsv(fileName):
	print('loading file ' + fileName)
	print(fileName)
	raw_data = open(fileName, 'rt')
	reader = csv.DictReader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
	items = list(reader)
	raw_data.close()
	return items

def writeCsv(fileName, header, items):
	print('writing file ' + fileName)
	csvfile = open(fileName, 'wt')
	writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_NONE, quotechar='', escapechar='\n',lineterminator='\n')
	writer.writerow(header)
	writer.writerows(items)
	csvfile.close()
