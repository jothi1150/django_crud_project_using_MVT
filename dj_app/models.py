
from django.db import models


class StudentData(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True
    )

    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    department = models.CharField(max_length=100)
    course = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
