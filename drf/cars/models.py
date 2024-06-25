from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=20)
    mark = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.brand} - {self.mark} | {self.year} | {self.price}'