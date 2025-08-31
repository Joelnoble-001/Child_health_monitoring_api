from django.db import models
from children.models import Child

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

class Immunization(models.Model):
    VACCINES = [("POLIO", "Polio"), ("BCG", "BCG"), ("MEASLES", "Measles")]
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="immunizations")
    vaccine_type = models.CharField(max_length=50, choices=VACCINES)
    date_given = models.DateField()

class ClinicVisit(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="visits")
    visit_date = models.DateField()
    reason = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

class WeightRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="growth_records")
    date_recorded = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    nutrition_status = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        self.nutrition_status = self.calculate_nutrition_status()
        super().save(*args, **kwargs)

    def calculate_nutrition_status(self):
        bmi = float(self.weight) / ((float(self.height)/100) ** 2)
        if bmi < 14: return "Underweight"
        elif bmi > 18: return "Overweight"
        return "Normal"
