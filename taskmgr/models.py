from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    joining_date = models.DateField()

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title

    def days_left(self):
        return (self.due_date - date.today()).days
    days_left.short_description = "Days Left"

    def clean(self):
        if self.status == "Pending" and self.employee_id:
            pending_count = Task.objects.filter(employee=self.employee, status="Pending").exclude(pk=self.pk).count()
            if pending_count >= 5:
                raise ValidationError("An employee cannot have more than 5 pending tasks.")

    # optional: ensure validation runs on save
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

# Create your models here.
