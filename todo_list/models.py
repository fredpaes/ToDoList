from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    LOCATION = (
        ('out', 'exterior'),
        ('in', 'interior'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    location = models.CharField(max_length=3, choices=LOCATION, default='in')
    cant = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)
