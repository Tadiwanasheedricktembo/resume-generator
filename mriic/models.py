from django.db import models


class Resume(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)

    education_level = models.CharField(max_length=150)
    skills = models.TextField()
    work_experience = models.TextField(blank=True)
    projects = models.TextField(blank=True)
    certifications = models.TextField(blank=True)
    languages = models.CharField(max_length=255, blank=True)

    linkedin_profile = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    portfolio_website = models.URLField(blank=True)

    passport_photo = models.ImageField(
        upload_to='passport_photos/',
        blank=True,
        null=True
    )

    generated_pdf = models.FileField(
        upload_to='generated_resumes/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
