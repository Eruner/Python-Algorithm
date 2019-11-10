import csvfiles
import datetime
import globals

def Results():
	header = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']
	printFile('centers', header, globals.centers)
	printFile('likeliness', header, globals.likeliness)

def printFile(label, header, items):
	fileName = timeStamped(label + '.csv')
	filePath = '..\output\\' + fileName
	csvfiles.writeCsv(filePath, header, items)

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)