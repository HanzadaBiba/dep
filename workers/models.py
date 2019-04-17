from django.db import models
from django.shortcuts import reverse
class Country(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Country'
class City(models.Model):

    name = models.CharField(max_length=255)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='city_country')
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'City'
class Position(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Position'
        verbose_name_plural='Position'
# Create your models here.
class Workers(models.Model):
    firstname=models.CharField(verbose_name='Name',max_length=255)
    lastname=models.CharField(max_length=255)
    fathername=models.CharField(max_length=255)
    position=models.ForeignKey(Position,on_delete=models.CASCADE,related_name='workers_position')
    slug=models.SlugField(max_length=255)
    image=models.ImageField(upload_to='workers/',blank=True)
    date_birn=models.DateField()
    gender=models.BooleanField(default=True)
    price=models.PositiveIntegerField()
    phone_number=models.CharField(max_length=12)
    home_phone_number=models.CharField(max_length=6)

    city=models.ForeignKey(City,on_delete=models.CASCADE,related_name='workers_city')
    adress=models.CharField(max_length=255)

    date_created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    def __str__(self):
        return '{} {} {}'.format(self.firstname,self.lastname,self.fathername)
    class Meta:
        ordering=['date_created']
        verbose_name='Workers'
        verbose_name_plural='Workers'
    def get_absolute_url(self):
        return reverse('workers_detail',args=[self.slug])
