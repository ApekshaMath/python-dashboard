from django.db import models

# Create your models here.

class Header(models.Model):
    header1 = models.CharField(max_length=250)
    header2 = models.CharField(max_length=250)
    header3 = models.CharField(max_length=250)
    header4 = models.CharField(max_length=250)
    header5 = models.CharField(max_length=250)
    header6 = models.CharField(max_length=250)

    def __str__(self):
        return self.header1
    

