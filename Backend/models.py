from django.db import models

# Create your models here.


class CatDb(models.Model):
    Cat_Name = models.TextField(max_length=100, null=True, blank=True)
    Language = models.CharField(max_length=100, null=True, blank=True)
    Genre = models.CharField(max_length=100, null=True, blank=True)


class MultiDb(models.Model):
    Multi_name = models.TextField(max_length=100, null=True, blank=True)
    Multi_lang = models.CharField(max_length=100, null=True, blank=True)
    Multi_genre = models.CharField(max_length=100, null=True, blank=True)
    Title = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(max_length=1000, null=True, blank=True)
    About = models.TextField(max_length=500, null=True, blank=True)
    Cast = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    File = models.FileField(upload_to="Multimedia", null=True, blank=True)


class MalDb(models.Model):
    MalTitle = models.CharField(max_length=50, null=True, blank=True)
    genre = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    cast = models.CharField(max_length=500, null=True, blank=True)
    time = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to="malayalam images", null=True, blank=True)
    vid = models.FileField(upload_to="malayalam videos", null=True, blank=True)



