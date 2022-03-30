from django.db import models


class Logo(models.Model):
    image = models.ImageField(upload_to='Logo/')

class ContactUs(models.Model):
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    

class Category(models.Model):
    name = models.CharField(max_length=200)

class VideoNews(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='VideoNews/')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300, blank=True, null=True)
    data = models.DateField(auto_now_add=True)

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='News/')
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    data = models.DateField(auto_now_add=True)

class Loyixalar(models.Model):
    image = models.ImageField(upload_to='Loyixalar/')
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    data = models.DateField(auto_now_add=True)
    

class XaftaNews(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='XaftaNews/')
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    data = models.DateField(auto_now_add=True)

class City(models.Model):
    name = models.CharField(max_length=200)

class Safarlar(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    video = models.FileField(upload_to="Safarlar/")
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=400)

class Category2(models.Model):
    name = models.CharField(max_length=200)
    
class Members(models.Model):
    category = models.ForeignKey(Category2, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Members/')
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)

class Channels(models.Model):
    image = models.ImageField(upload_to='Channels/')

class Conntecting(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()