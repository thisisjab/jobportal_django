from django.db import models
from django.contrib.auth import get_user_model


class JobCandidate(models.Model):
    age = models.DateField(blank=True, null=True)
    short_bio = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.OneToOneField(
        get_user_model(), primary_key=True, on_delete=models.CASCADE)
    

class Employer(models.Model):
    short_bio = models.CharField(max_length=150, blank=True, null=True)
    user = models.OneToOneField(
        get_user_model(), primary_key=True, on_delete=models.CASCADE)


class Company(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    manager = models.ForeignKey(Employer, on_delete=models.CASCADE)


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='jobs')


class JobApplication(models.Model):
    STATUS_APPROVED = 'approved'
    STATUS_PENDING = 'pending'
    STATUS_REJECTED = 'rejected'
    STATUS_CHOICES = [
        (STATUS_APPROVED, 'Approved'),
        (STATUS_PENDING, 'Pending'),
        (STATUS_REJECTED, 'Rejected'),
    ]
    job = models.ForeignKey(Job, on_delete=models.PROTECT,
                            related_name='applications')
    candidate = models.ForeignKey(
        JobCandidate, on_delete=models.CASCADE, related_name='job_applications')
    submition_date = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_APPROVED)
    message = models.TextField(null=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.status != self.STATUS_PENDING and self.message is None:
            raise ValidationError(message='Message is required.')
        return super().clean()
