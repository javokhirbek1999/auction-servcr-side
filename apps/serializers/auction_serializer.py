from django.utils.translation import gettext_lazy as _

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
        fields = ('id', 'owner', 'get_owner_details', 'name', 'description', 'thumbnail', 'category', 'price', 'currency', 'endDate', 'status')


    def create(self, validated_data):
        return super().create(validated_data)   
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class BidSerializer(serializers.ModelSerializer):

    """ Serializer for Bid Model """

    class Meta:
        model = Bid
        fields = ('id', 'get_bidder_details', 'get_item_details', 'item', 'bidder', 'bidPrice', 'bidDate', 'status')
        extra_kwargs = {
            'item': {'write_only':True,},
            'bidder': {'write_only':True,},
            'get_item_details': {'read_only': True},
        }


    def validate(self, attrs):
        itemPrice = attrs.get('item').price
        bidPrice = attrs.get('bidPrice')

        itemPrice = float(itemPrice)
        bidPrice = float(bidPrice)

        if bidPrice < itemPrice:
            raise serializers.ValidationError(_('Bid price must be greater than or equal to the item price'))
        
        return attrs
    
    def create(self, validated_data):
        return super().create(validated_data)

    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)