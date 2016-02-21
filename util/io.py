class IOManager:
    fileContent = []
    
    def __init__(self, filename):
        self.filename = filename
        self.readFile()
        
    def printFilename(self):
        print self.filename
        
    def printFileContent(self):
        print IOManager.fileContent
        
    #for now, read the entire file
    #TODO: line by line into 'bucket' files on disk
    #This is a ram vs disk space issue
    #for now, assume infinite memory
    
    def readFile(self):
        with open(self.filename, "r") as file:
            IOManager.fileContent = file.read().splitlines()
        
        