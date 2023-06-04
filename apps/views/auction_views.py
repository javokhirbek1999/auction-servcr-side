from rest_framework import generics, permissions

from ..permissions.auction_permissions import IsAdminOrReadOnly
from ..serializers.auction_serializer import CategorySerializer, ItemSerializer, BidSerializer
from ..models.auction import Category, Item, Bid


class CategoryView(generics.ListCreateAPIView):

    """
    API View for Category Model
    """
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AuctionView(generics.ListCreateAPIView):

    """
    API View for Auction Model
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class UserAuctions(generics.ListCreateAPIView):

    """
    API View for Managing auctions
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return Item.objects.filter(auctioneer__user_name=self.kwargs.get('username'))


class SingleUserAuction(generics.RetrieveUpdateDestroyAPIView):

    """
    API View for single auction view
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ItemSerializer

    def get_object(self):
        return Item.objects.get(auctioneer__user_name=self.kwargs.get('username'),id=self.kwargs.get('pk'))



class AllBidsView(generics.ListCreateAPIView):

    """
    API View for Bid Model
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BidSerializer
    queryset = Bid.objects.all()


class BidsView(generics.ListAPIView):

    """
    API VIew for Bid Model
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BidSerializer

    def get_queryset(self):
        return Bid.objects.filter(item__id=self.kwargs.get('pk')).order_by('-bidPrice')


