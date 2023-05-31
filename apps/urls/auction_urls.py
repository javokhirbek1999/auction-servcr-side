from django.urls import path

from ..views.auction_views import CategoryView, AuctionView, AllBidsView, BidsView


urlpatterns = [
    path('', AuctionView.as_view(), name='auction'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('bids/', AllBidsView.as_view(), name='all-bids'),
    path('bids/<str:pk>', BidsView.as_view(), name='bids')
]