from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


currencies = (
    ('EUR', 'EUR'),
    ('USD', 'USD'),
    ('PLN', 'PLN')
)

bidStatuses = (
    ('Sold','Sold'),
    ('Bid','Bid'),
    ('Cancelled', 'Cancelled'),
)


class Category(models.Model):
    name = models.CharField(max_length=200)


    class Meta:
        verbose_name_plural = 'Categories'
    

    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    auctioneer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField()
    thumbnail = models.URLField(default='https://ingoodcompany.asia/images/products_attr_img/matrix/default.png')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=999)
    currency = models.CharField(max_length=3, choices=currencies)
    endDate = models.DateTimeField()


    def __str__(self) -> str:
        return f'{self.id}-{self.name} | {self.price} {self.currency} | {self.endDate} | {self.auctioneer.user_name}'

    @property
    def get_auctioneer_details(self):

        return {
            'first_name': self.auctioneer.first_name,
            'last_name': self.auctioneer.last_name,
            'user_name': self.auctioneer.user_name,
            'email': self.auctioneer.email,
            'date_joined': self.auctioneer.date_joined,
            'date_updated': self.auctioneer.date_updated
        }


class Bid(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    bidder = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    bidPrice = models.DecimalField(decimal_places=2, max_digits=999)
    bidDate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=bidStatuses)

    def __str__(self) -> str:
        return f'{self.item.id} - {self.item.name} | {self.bidder.user_name} | {self.bidPrice} | {self.bidDate} | {self.status}'

    @property
    def get_item_details(self):
        return {
            'name': self.item.name,
            'description': self.item.description,
            'thumbnail': self.item.thumbnail.url,
            'category': self.item.category.name,
            'price': self.item.price,
            'currency': self.item.currency,
            'endDate': self.item.endDate
        }
    
    @property
    def get_bidder_details(self):
        return {
            'first_name': self.bidder.first_name,
            'last_name': self.bidder.last_name,
            'user_name': self.bidder.user_name,
            'email': self.bidder.email,
            'date_joined': self.bidder.date_joined,
            'date_updated': self.bidder.date_updated
        }
