from django.db import models

# Create your models here.


class Candidate(models.Model):
    
    name = models.CharField(max_length=100)
    available_from = models.TimeField()
    available_to = models.TimeField()

def __str__(self):
    return str(self.name)


class Interviewer(models.Model):
    
    name = models.CharField(max_length=100)
    available_from = models.TimeField()
    available_to = models.TimeField()
def __str__(self):
    return str(self.name)