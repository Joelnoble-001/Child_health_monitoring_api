from django.db import models

# Create your models here.

class Caregiver(models.Model):
    name = models.CharField(max_length=200)
    relationship_to_child = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Child(models.Model):
    GENDER_CHOICES = [("M", "Male"), ("F", "Female")]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, related_name="children")
    address = models.TextField(blank=True)
    community = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
