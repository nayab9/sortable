#this class will take a JSON data structure and attempt
# to create a dict with the key being 'model'
from collections import defaultdict

class ModelMaker:

    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.modelDict = defaultdict(list)
        self.createModelDict()
    
    #Check for duplicates of model/manufacturer? i.e. if it doesn't exist, add it?
    def createModelDict(self):
        #print "Asking for a dict creation"
        #self.modelDict = defaultdict(list)
        for item in self.jsonData:
            #print item['model']
            self.modelDict[item['model']].append(item)
        #print "printing newly constructed product index: ", self.modelDict