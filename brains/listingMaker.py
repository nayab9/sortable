# This class will identify matching model numbers, then
# identify matching manufacturers to determine a listing match

from collections import defaultdict
from util.jsonParser import JSONParser
import os

class ListingMaker:
    
    # Constructor will have access to the products and listings
    def __init__(self, listings, products):
        self.listings = listings
        self.products = products
        # Store our results in this dictionary
        self.resultDict = defaultdict(list)
        # Trigger the filtering process
        #self.createResultsListRam()
 
    # Begins parsing the listings for products
    def createResultsListRam(self):
        # Iterate over all listings
        for listing in self.listings:
            # Split listings into keywords for which we can play with
            splitString = listing['title'].split()
            for word in splitString:
                if word in self.products:
                    for element in self.products[word]:
                        if listing['manufacturer'].find(element['manufacturer']) != -1:
                            self.resultDict[element['product_name']].append(listing)
    
    # implement a disk heavy solution
    def createResultsListDisk(self):
        lineParser = JSONParser("")
        dir = "./cache/"
                
        with open(self.listings, "r") as file:
            for newLine in file:
                # newLine has a title field I need to parse
                #print "newline: ", newLine
                #line = lineParser.parseJSONString(file.readline().lower())
                line = lineParser.parseJSONString(newLine.lower())
                
                splitString = line['title'].split()
                                
                temp_dir = dir + line['manufacturer'] + ".txt"
                try:
                    with open(temp_dir, "r") as filePointer:
                        for product in filePointer:
    
                            product = lineParser.parseJSONString(product.lower())
                            
                            for word in splitString:
                                if product['model'].find(word) != -1:
                                    print "yay"
                                    try:
                                        with open('results.txt', "r") as resultsPointer:
                                            print "did i reach this at least..."
                                            if (os.stat("results.txt").st_size == 0):
                                                print "empty file, adding my junk"
                                                self.resultDict[product['model']].append(line)
                                            else:
                                                for resultsLine in resultsPointer:
                                                    #line = lineParser.parseJSONString(file.readline().lower())
                                                    resultsLine = lineParser.parseJSONString(newLine.lower())
                                                    print "result line? ", resultsLine
                                                    if product['model'] in resultsLine:
                                                        print "anything in results line? "
                                                        self.resultDict = resultsLine
                                                        self.resultDict[product['model']].append(line)
                                                    else:
                                                        print "nothing was in results line."
                                                        self.resultDict[product['model']].append(line)
                                        resultsPointer.close()
                                        try:
                                            with open('results.txt', "w") as resultsPointer:
                                                print "heres my result dict", self.resultDict  
                                                try:
                                                    json.dump(self.resultDict, resultsPointer)
                                                except:
                                                    print "there error was: "
                                                print "dumped out file"
                                                self.resultDict.clear()
                                                print "clearing.."
                                        except:
                                            print "failed to open results.txt for writing"
                                    except:
                                        print "failed to open results.txt for reading"
                                        #json.dump(self.listOutput, filePointer, indent=2)
                except:
                    pass
                    #print "Unsupported manufactuer"
                    #json.dump(line, filePointer)
                    #filePointer.write(os.linesep)
    
    
    
    
    # implement a load balanced solution