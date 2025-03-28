from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Store
from wishlists.models import Wishlist

from geopy.distance import geodesic

class StoreDetailSerializer(ModelSerializer):

    rating = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = (
            "id",
            "pk",
            "p_name",
            "p_startdate",
            "p_enddate",
            "img_url",
            "news_url",
            "p_location",
            "p_hashtag",
            "rating",
            "status",
            "thumbnail",
            "frontLat",
            "frontLon",
            "is_liked",
        )
        #depth = 1

    def get_rating(self, store): #get_필드이름으로 고정시켜야한다. #두번째 인자는 모델이름이 된다.
        return store.rating()
    
    def get_status(self, store):
        return store.status()
    
    def get_is_liked(self, store):
        user = self.context['request'].user
        return store.is_liked(user)
    
class StoreListSerializer(ModelSerializer):
    # rating = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    # is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = (
            "id",
            "pk",
            "p_name",
            "p_startdate",
            "p_enddate",
            "p_location",
            "p_hashtag",
            # "rating",
            "status",
            "thumbnail",
            # "is_liked",
        )
        #depth = 1
    
    # def get_rating(self, store):
    #     return store.rating()
    
    def get_status(self, store):
        return store.status()
    
    # def get_is_liked(self, store):
    #     user = self.context['request'].user
    #     return store.is_liked(user)
    
class TinyStoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = (
            "id",
            "pk",
            "p_name",
            )

class StoreNearSerializer(ModelSerializer):
    status = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = (
            "id",
            "pk",
            "p_name",
            "p_startdate",
            "p_enddate",
            "p_location",
            "p_hashtag",
            "status",
            "thumbnail",
            "distance",
        )

    def get_status(self, store):
        return store.status()
    
    def get_distance(self, obj):
        # 사용자의 현재 위치
        user_location = self.context['user_location']
        store_location = (obj.frontLat, obj.frontLon)

        # 거리를 계산하여 반환합니다.
        distance = geodesic(user_location, store_location).kilometers
        return distance
    