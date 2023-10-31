from django.db import models
from django.contrib.auth.models import User

class TimeOffRequest(models.Model):
    REQUEST_TYPES = (
        ('paid', 'Paid Time Off'),
        ('sick', 'Sick Time Off'),
        ('unpaid', 'Unpaid Time Off'),
        ('compensatory', 'Compensatory Time Off'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=12, choices=REQUEST_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.request_type} - {self.start_date} to {self.end_date}"

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title