from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'name',
            'email',
            'address',
            'phone_number',
            'education_level',
            'skills',
            'work_experience',
            'projects',
            'certifications',
            'languages',
            'linkedin_profile',
            'github_profile',
            'portfolio_website',
            'passport_photo',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'education_level': forms.TextInput(attrs={'class': 'form-control'}),

            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'work_experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'projects': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'certifications': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'languages': forms.TextInput(attrs={'class': 'form-control'}),

            'linkedin_profile': forms.URLInput(attrs={'class': 'form-control'}),
            'github_profile': forms.URLInput(attrs={'class': 'form-control'}),
            'portfolio_website': forms.URLInput(attrs={'class': 'form-control'}),
            'passport_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }