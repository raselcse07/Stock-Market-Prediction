from django.db import models


class Company(models.Model):

    company_Name    =models.CharField(max_length=250)
    month           =models.DateField(auto_now=False, auto_now_add=False)
    rising          =models.CharField(max_length=250)
    down            =models.CharField(max_length=250)


    class Meta:
         ordering=["-rising"]

    def __str__(self):

        return self.company_Name
