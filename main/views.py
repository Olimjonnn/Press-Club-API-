from os import access
from unicodedata import category
from aiohttp import request
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from main.models import *
from main.serializer import *


class LogoView(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    http_method_names = ['get']

    def list(self, request):
        logo = Logo.objects.last()
        log = LogoSerializer(logo)
        return Response(log.data)


class ContactUsView(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    http_method_names = ['get']


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class VideoNewsView(viewsets.ModelViewSet):
    queryset = VideoNews.objects.all()
    serializer_class = VideoNewsSerializer

    def create(slef, request):
        try:
            VideoNews.objects.create(
                category_id = request.POST.get("category"),
                video = request.FILES['video'],
                title = request.data['title'],
                text = request.data['text'],
            )
            return Response({"Created"})
        except Exception as arr:
            data = {
                "error":f"{arr}"
            }
            return Response(data)


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    http_method_names = ['get']

    @action(['GET'], detail=False)
    def find(self, request):
        try:
            category = request.GET.get('category')
            a = News.objects.filter(category_id=category)
            b = NewsSerializer(a, many=True)
            return Response(b.data)
        except Exception as arr:
            return Response(arr)


class LoyixalarView(viewsets.ModelViewSet):
    queryset = Loyixalar.objects.all()
    serializer_class = LoyixalarSerializer

    http_method_names = ['get']


class XaftaNewsView(viewsets.ModelViewSet):
    queryset = XaftaNews.objects.all()
    serializer_class = XaftaNewsSerializer
    http_method_names = ['get']
    def list(self, request):
        xaftanews = XaftaNews.objects.all().order_by("-id")[0:6]
        xafta = XaftaNewsSerializer(xaftanews, many=True)
        return Response(xafta.data)



class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SafarlarView(viewsets.ModelViewSet):
    queryset = Safarlar.objects.all()
    serializer_class = SafarlarSerializer
    
    def create(self, request):
        Safarlar.objects.create(
            city_id = request.data['city'],
            video = request.data['video'],
        )
        return Response({"CREATED"})
    

class SafarTextView(viewsets.ModelViewSet):
    queryset = SafarText.objects.all()
    serializer_class = SafarTextSerializer

    @action(['GET'], detail=False)
    
    def new(self, request):
        try:
            video = request.GET.get('video')
            sar = Safarlar.objects.get(id=video)
            v = SafarText.objects.filter(sar=video.c.id)
            a = SafarTextSerializer(v, many=True)
            return Response(a.data)

        except Exception as arr:
            data = {
                "error":f"{arr}"
            }
            return Response(data)

    def create(self, request):
        try:
            SafarText.objects.create(
                video_id = request.data['video'],
                title = request.data['title'],
                text = request.data['text'],
            )
            return Response({"CREATED"})
        except Exception as arr:
            return Response(arr)




class Category2View(viewsets.ModelViewSet):
    queryset = Category2.objects.all()
    serializer_class = Category2Serializer


class MembersView(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer


class ChannelsView(viewsets.ModelViewSet):
    queryset = Channels.objects.all()
    serializer_class = ChannelsSerializer


class ConntectingView(viewsets.ModelViewSet):
    queryset = Conntecting.objects.all()
    serializer_class = ConntectingSerializer

