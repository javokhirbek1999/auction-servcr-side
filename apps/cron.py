from .models.auction import Item
from datetime import datetime


def checkExpiredAuctions():
    
    # Query all expired auctions
    allExpiredAuctions = Item.objects.filter(endDate__lte=datetime.now())

    # Remove all expired auction from database
    for auction in allExpiredAuctions:
        auction.delete()
    
