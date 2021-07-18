from django.db import models

# Create your models here.
class transectiondetail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    deb_amt = models.IntegerField()
    cr_amt = models.IntegerField()
    ac_bal = models.IntegerField()

class customerdetail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    avail_bal = models.IntegerField()