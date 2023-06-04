from django.urls import path

from ..views.auction_views import CategoryView, AuctionView, AllBidsView, BidsView, UserAuctions, SingleUserAuction, SellTheItem


urlpatterns = [
    path('', AuctionView.as_view(), name='auction'),
    path('users/<str:username>/', UserAuctions.as_view(), name='user-auctions'),
    path('users/<str:username>/<str:pk>', SingleUserAuction.as_view(), name='user-single-auction'),
    path('users/<str:username>/<str:pk>/sell', SellTheItem.as_view(), name='sell-the-item'),
    path('categories/all', CategoryView.as_view(), name='categories'),
    path('bids/all/', AllBidsView.as_view(), name='all-bids'),
    path('bids/all/<str:pk>', BidsView.as_view(), name='bids'),
]