#this class will handle the main logic of identifying a product to a Listing
#Given a list of all products which can be indexed by their model, do the following:
# First, parse the listing to try and gain some knowledge as to what product it is
# We will first attempt to match the model number to the Listing
# if the model number is not unique, we then try to match a manufacturer to the Listing
# if we successfully match the model to a unique model, we win... alternatively
# if we match a model ANd a manufacter, we win.
from collections import defaultdict

class ListingMaker:
    
    def __init__(self, listings, products):
        self.listings = listings
        self.resultDict = defaultdict(list)
        self.products = products
        self.createResultsList()
        
    def createResultsList(self):
        for item in self.listings:
            splitString = item['title'].split()
            for word in splitString:
                if word in self.products:
                    #print "I found a keyword in a listing which matches a model"
                    #print self.products
                    #print self.products[word]
                    #print len(self.products[word])
                    if len(self.products[word]) == 1:
                        #print "Only one model entry!, match found!"
                        self.resultDict[self.products[word][0]['product_name']].append(item)
                        print self.resultDict
                    elif len(self.products[word]) > 1:
                        print "More than one model match, manufacter filter required"
                #else:
                    #print "bummer!"