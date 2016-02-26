import json
import os
import shutil
from collections import defaultdict
from util.jsonParser import JSONParser

class IOManager:
    
    def __init__(self, filename):
        self.filename = filename
        self.fileContent = ""
        #self.outFormatted = {}
        self.listOutput = [] #defaultdict(list)
       # self.readFileIntoRam()
        
    def printFilename(self):
        print self.filename
        
    def printFileContent(self):
        print self.fileContent
        
    # Reads entire product file into RAM
    def readFileIntoRam(self):
        with open(self.filename, "r") as file:
           # lines = file.readlines()
          #  for line in lines:
           #     line = line.lower()
           #     self.fileContent = self.fileContent + line;
        #print self.fileContent
        
            self.fileContent = file.read().splitlines()
            self.fileContent = [element.lower() for element in self.fileContent]
            #print self.fileContent
    
    # Writes entire content to file
    def writeFileUsingRam(self, outData):

        for product, listings in outData.items():
            outFormatted = {}
            outFormatted['product_name'] = product
            outFormatted['listings'] = listings
            self.listOutput.append(outFormatted)
        with open('results.txt', "w") as filePointer:
            json.dump(self.listOutput, filePointer, indent=2)
        
        print "number of items in output file:", len(self.listOutput)

    # Reads only one product at a time and dumps into bucket on disk
    def readFileOntoDisk(self, field):
        lineParser = JSONParser("")
        dir = "./cache/"
        if os.path.exists(dir):
            shutil.rmtree(dir)
            
        while os.path.exists(dir): # check if it exists
            pass
        
        os.makedirs(dir)
            
        with open(self.filename, "r") as file:
            for newLine in file:
                #line = lineParser.parseJSONString(file.readline().lower())
                line = lineParser.parseJSONString(newLine.lower())
                temp_dir = dir + line[field] + ".txt"

                with open(temp_dir, "a+") as filePointer:
                    json.dump(line, filePointer)
                    filePointer.write(os.linesep)