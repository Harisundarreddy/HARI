from django.db import models
from django.urls import reverse

# Create your models here.
class P(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    phoneno=models.IntegerField()
    age=models.IntegerField()
    J_date=models.DateField()
    symptoms=models.CharField(max_length=200)
    prescription=models.CharField(max_length=200)

    def get_absolute_url(self,**kwargs):
        return reverse('pa',kwargs={'pk':self.id})
