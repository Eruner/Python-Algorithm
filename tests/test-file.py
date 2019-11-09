import sys
sys.path.append('..\logic')
import csvfiles

def createTestFile():
	fileName = '..\output\DeleteMePlease.txt'
	header = ['Name','number']
	items = []
	items.append(['car', '4'])
	items.append(['animal', '7'])
	items.append(['human', '47'])
	csvfiles.writeCsv(fileName, header, items)

createTestFile()
