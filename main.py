from util.io import IOManager
from util.jsonParser import JSONParser

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
parsedData1 = JSONParser(fileInput1.fileContent)
#parsedData1.printData()

#now have a data structure containing all data of products


#Go through each product, and make a dict with key being the manufacturer

#go through each listing, send the listing to a parser

#the parser will take the listing, pull its 'title'
#the title for the list is split into its keywords based on some criter
#the split words are then compared to the manufacters products 
#first try to find product name, family, then model
#if all three match, we are surely confident that this is the correct listing





#output file to json at the end