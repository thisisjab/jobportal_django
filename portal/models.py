from django.db import models
from django.contrib.auth import get_user_model


class JobCandidate(models.Model):
    birth_date = models.DateField(blank=True, null=True)
    short_bio = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.OneToOneField(
        get_user_model(), primary_key=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Job Candidate'
        verbose_name_plural = 'Job Candidates'

    def __str__(self):
        return f'{self.user.username} | {self.user.first_name} {self.user.last_name}'
    

class Employer(models.Model):
    short_bio = models.CharField(max_length=150, blank=True, null=True)
    user = models.OneToOneField(
        get_user_model(), primary_key=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

    def __str__(self):
        return f'{self.user.username} | {self.user.first_name} {self.user.last_name}'


class Company(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    manager = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='companies')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.title
    

class JobCategory(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Job Category'
        verbose_name_plural = 'Job Categories'

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(JobCategory, on_delete=models.PROTECT, related_name='jobs')
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='jobs')
    
    class Meta:
        permissions = [('can_post_jobs', 'Can add new job posts')]
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return f'{self.title} | {self.company.title}'


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
        max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'

    def __str__(self):
        return str(self.pk)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.status != self.STATUS_PENDING and not self.message:
            raise ValidationError(message='Message is required.')
        return super().clean()
