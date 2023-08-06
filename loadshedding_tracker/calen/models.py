from django.db import models

class Outage(models.Model):
    ward_number = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Ward {self.ward_number} - {self.date}"