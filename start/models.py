from django.db import models

# Create your models here.
from django.db import models

class ProfessorStudent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    number = models.FloatField()
    position = models.CharField(max_length=100)
    age = models.FloatField()
    height = models.CharField(max_length=100)
    weight = models.FloatField()
    college = models.CharField(max_length=100, null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)

