# This class will identify matching model numbers, then
# identify matching manufacturers to determine a listing match

from collections import defaultdict

class ListingMaker:
    
    # Constructor will have access to the products and listings
    def __init__(self, listings, products):
        self.listings = listings
        self.products = products
        # Store our results in this dictionary
        self.resultDict = defaultdict(list)
        # Trigger the filtering process
        self.createResultsListRam()
 
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
    
    # implement a load balanced solution