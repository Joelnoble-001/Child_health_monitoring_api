from django.db import models

# Create your models here.
class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    guardian_name = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class HealthRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="health_records")
    height = models.FloatField()
    weight = models.FloatField()
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

class Vaccination(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="vaccinations")
    vaccine_name = models.CharField(max_length=100)
    date_administered = models.DateField()
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("done", "Done")])
