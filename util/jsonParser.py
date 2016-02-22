import json

class JSONParser:
    
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.parsedData = []
        #print "JSON input", jsonData
        self.parseJSON()
        
    def parseJSON(self):
        #print "parsing json data now"
        
        for line in self.jsonData:
            self.parsedData.append(json.loads(line))
    
    def printData(self):
        #print "printing the so called parsed data"
        #print self.parsedData
        blah = ""