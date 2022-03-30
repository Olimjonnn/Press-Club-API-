from rest_framework import serializers
from main.models import *

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"
        

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class VideoNewsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = VideoNews
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

class LoyixalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loyixalar
        fields = "__all__"

class XaftaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = XaftaNews
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = City
        fields = "__all__"

class SafarlarSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Safarlar
        fields = "__all__"


class Category2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category2
        fields = "__all__"

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = "__all__"

class ChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = "__all__"

class ConntectingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conntecting
        fields = "__all__"
