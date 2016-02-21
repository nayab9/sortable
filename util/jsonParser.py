import json

class JSONParser:
    parsedData = []
    
    def __init__(self, jsonData):
        self.jsonData = jsonData
        #print "JSON input", jsonData
        self.parseJSON()
        
    def parseJSON(self):
        #print "parsing json data now"
        
        for line in self.jsonData:
            JSONParser.parsedData.append(json.loads(line))
    
    def printData(self):
        print "printing the so called parsed data"
        print JSONParser.parsedData