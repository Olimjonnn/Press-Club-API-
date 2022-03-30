from tkinter.tix import DirTree
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
            title = request.data['title'],
            text = request.data['text'],
        )
        return Response({"CREATED"})
    
    @action(['GET'], detail=False)
    def new(self, request):
        city = request.GET.get("city")
        ct = Safarlar.objects.filter(city_id=city)
        c = SafarlarSerializer(ct , many=True)
        return Response(c.data)

    




class Category2View(viewsets.ModelViewSet):
    queryset = Category2.objects.all()
    serializer_class = Category2Serializer


class MembersView(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    
    def create(self, request):
        Members.objects.create(
            category_id = request.data['category'],
            image = request.FILES['image'],
            name = request.data['name'],
            job = request.data['job'],
            text = request.data['text']
        )
        return Response("Created")

    @action(['GET'], detail=False)
    def fff(self, request):
        category = request.GET.get("category")
        cate = Members.objects.filter(category_id=category)
        cat = MembersSerializer(cate, many=True)
        return Response(cat.data)
        


class ChannelsView(viewsets.ModelViewSet):
    queryset = Channels.objects.all()
    serializer_class = ChannelsSerializer

    http_method_names = ['get']

class ConntectingView(viewsets.ModelViewSet):
    queryset = Conntecting.objects.all()
    serializer_class = ConntectingSerializer

    http_method_names = ['post']
