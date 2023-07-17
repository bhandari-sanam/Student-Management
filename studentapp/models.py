from django.db import models

# Create your models here.
gender_choice = (
    ("male","Male"),
    ("female","Female")
    
)
class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    # grade = models.IntegerField()
    section = models.CharField(max_length=200)
    # roll_no = models.IntegerField()
    status = models.CharField(
        ("Gender"), max_length= 220, choices=gender_choice\
        ,null=True , blank= True
    )
