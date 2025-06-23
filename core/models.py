from django.db import models

class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)
    buy_link = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Interest, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    preferences = models.ManyToManyField(Interest)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
