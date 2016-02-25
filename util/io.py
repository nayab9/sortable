import json
from collections import defaultdict

class IOManager:
    
    def __init__(self, filename):
        self.filename = filename
        self.fileContent = ""
        #self.outFormatted = {}
        self.listOutput = [] #defaultdict(list)
        self.readFile()
        
    def printFilename(self):
        print self.filename
        
    def printFileContent(self):
        print self.fileContent
        
    #for now, read the entire file
    #TODO: line by line into 'bucket' files on disk
    #This is a ram vs disk space issue
    #for now, assume infinite memory
    
    def readFile(self):
        with open(self.filename, "r") as file:
           # lines = file.readlines()
          #  for line in lines:
           #     line = line.lower()
           #     self.fileContent = self.fileContent + line;
        #print self.fileContent
        
            self.fileContent = file.read().splitlines()
            self.fileContent = [element.lower() for element in self.fileContent]
            #print self.fileContent
        
    def writeFileUsingRam(self, outData):
        # go through the JSON and arrange it differently?
        #print outData
        
        for product, listings in outData.items():
            outFormatted = {}
            outFormatted['product_name'] = product
            outFormatted['listings'] = listings
            self.listOutput.append(outFormatted)
        with open('results.txt', "w") as filePointer:
            json.dump(outData, filePointer, indent=2)