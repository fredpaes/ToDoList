from django.db import models

# Create your models here.
class List(models.Model):
    LOCATION = (
        ('out', 'exterior'),
        ('in', 'interior'),
    )
    item = models.CharField(max_length=100)
    location = models.CharField(max_length=3, choices=LOCATION, default='in')
    cant = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)
