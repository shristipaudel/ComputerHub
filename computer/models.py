from django.db import models

# Create your models here.


class ComputerBrands(models.Model):
    brandname = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_computerbrands():
        return ComputerBrands.objects.all()

    def __str__(self):
        return self.brandname


class ComputerSpecification(models.Model):
    generation = models.CharField(max_length=50)
    price_min = models.IntegerField(default=0)
    price_max = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
    brandname = models.ForeignKey(ComputerBrands, on_delete=models.CASCADE)
    computercode=models.IntegerField(default=0)

    @staticmethod
    def get_all_computerspecifications():
        return ComputerSpecification.objects.all()

class Order(models.Model):
    computercode=models.CharField(max_length=50,null=True,blank=True)
    brandname = models.CharField(max_length=50, null=True, blank=True)
    QUANTITY_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    quantity = models.CharField(
        max_length=5, choices=QUANTITY_CHOICES, default='1')
    unitrate = models.CharField(max_length=50, default='')
    totalprice = models.CharField(max_length=40, default='')

    def register(self):
        self.save()
