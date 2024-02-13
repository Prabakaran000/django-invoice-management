from django.db import models

class Record(models.Model):
    S_No = models.AutoField(primary_key=True)
    consignment_No = models.CharField(max_length=100)
    date = models.DateField(auto_now_add = True)
    weight = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.consignment_No} {self.date}")