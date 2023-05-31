from apps.models.auction import Item
from django.utils import timezone


def checkExpiredAuctions():
    print("Running Cronjobs")
    # Query all expired auctions
    allExpiredAuctions = Item.objects.filter(endDate__lt=timezone.now())

    # Remove all expired auction from database
    for auction in allExpiredAuctions:
        auction.delete()
    
