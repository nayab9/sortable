from util.io import IOManager

#intialize IO manager with a filename (hardcoded for now)
#TODO: pass filename as a paramter with a flag
fileInput1 = IOManager("products.txt")
fileInput1.printFilename()
#fileInput1.printFileContent()

#intialize IO manager with a filename (hardcoded for now)
#TODO: pass filename as a paramter with a flag
fileInput2 = IOManager("listings.txt")
fileInput2.printFilename()
#fileInput2.printFileContent()

#send fileinput to a json parser which will handle processing data

#output file to json at the end