from __future__ import unicode_literals
from django.db import models

class Student(models.Model):
    cpf = models.IntegerField()
    dob = models.DateField()
    class Meta:
        db_table = "student"




   # month = models.ChoiceField()
    #year = models.IntegerField()

