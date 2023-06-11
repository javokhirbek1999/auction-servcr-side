from apps.models.auction import Item, Bid
from django.utils import timezone


def checkExpiredAuctions():
    print("Running Cronjobs")
    # Query all expired auctions
    allExpiredAuctions = Item.objects.filter(endDate__lt=timezone.now())

    # Remove all expired auction from database
    for auction in allExpiredAuctions:
        
        # Check the bids for all of the expired auctions
        # Sell the item for the highest bid if the highest bid's price is equal to or more than the item's price
        allBidsForThisAuction = Bid.objects.filter(item__id=auction.id).order_by('-bidPrice')

        if allBidsForThisAuction.first().bidPrice >= auction.price:
            auction.owner = allBidsForThisAuction.first().bidder
            auction.status = 'Sold'
            auction.save()
        else:
            auction.status = 'Cancelled'
            auction.delete()
        
    
