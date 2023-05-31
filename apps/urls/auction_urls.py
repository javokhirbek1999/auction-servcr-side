from django.urls import path

from ..views.auction_views import CategoryView, AuctionView, BidsView


urlpatterns = [
    path('', AuctionView.as_view(), name='auction'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('bids/', BidsView.as_view(), name='bids')
]