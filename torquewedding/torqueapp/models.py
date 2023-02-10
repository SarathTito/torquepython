from django.db import models

# Create your models here.
class Func(models.Model):
    name=models.CharField(max_length=250)
    cust=models.TextField()
    disc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=250)
    place = models.TextField()
    mobile = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
