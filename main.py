from util.io import IOManager
from util.jsonParser import JSONParser
from brains.modelMaker import ModelMaker
from brains.listingMaker import ListingMaker

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
parsedData2 = JSONParser(fileInput2.fileContent)
#now have a data structure containing all data of products

#Go through each product, and make a dict with key being the MODEL NUMBER!
modelDict = ModelMaker(parsedData1.parsedData)

# now I have a nice hash table of my products (note, this could be huge, putting it on disk in buckets is a ram efficient solution

#go through each listing.txt item, send the listing to a parser
listingList = ListingMaker(parsedData2.parsedData, modelDict.modelDict)

#the parser will take the listing, pull its 'title'
#the title for the list is split into its keywords based on some critera
#the split words are then compared to the MODELSs 
#first try to find MODEL - if multiple MODELs, match MANUFACTERUR
#if MODEl matches and is unique, THATSS the one 
#if multiple model matches, match the manufacter... thats the one


#output file to json at the end
fileInput1.writeFile(listingList.resultDict)

print listingList.resultDict
#fileInput1.writeFile({'blah':'blah2'})
