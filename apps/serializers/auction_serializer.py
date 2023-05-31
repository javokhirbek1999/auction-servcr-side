from rest_framework import serializers

from ..models.auction import Category, Item, Bid


class CategorySerializer(serializers.ModelSerializer):

    """ Serializer for Category Model """

    class Meta:
        model = Category
        fields = ('id', 'name')
    

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ItemSerializer(serializers.ModelSerializer):

    """ Serializer for Item Model """

    class Meta:
        model = Item
        fields = ('id', 'get_auctioneer_details', 'name', 'description', 'thumbnail', 'category', 'price', 'currency', 'endDate')


    def create(self, validated_data):
        return super().create(validated_data)   
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class BidSerializer(serializers.ModelSerializer):

    """ Serializer for Bid Model """

    class Meta:
        model = Bid
        fields = ('id', 'get_bidder_details', 'bidPrice', 'bidDate', 'status')
    
    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)