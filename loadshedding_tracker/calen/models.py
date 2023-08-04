from django.db import models

# Create your models here.

class days(models.Model):
    day = models.CharField(max_length=10)
    date = models.IntegerField()
    month = models.CharField(max_length=10)
    year = models.IntegerField()
    loadshedding = models.CharField(max_length=10)

    def __str__(self):
        return self.day + ' ' + str(self.date) + ' ' + self.month + ' ' + str(self.year) + ' ' + self.loadshedding
