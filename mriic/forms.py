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
            'name': forms.TextInput(attrs={'class': 'field-control', 'placeholder': 'Jane Doe'}),
            'email': forms.EmailInput(attrs={'class': 'field-control', 'placeholder': 'jane@example.com'}),
            'address': forms.TextInput(attrs={'class': 'field-control', 'placeholder': '123 Main Street, City'}),
            'phone_number': forms.TextInput(attrs={'class': 'field-control', 'placeholder': '(123) 456-7890'}),
            'education_level': forms.TextInput(attrs={'class': 'field-control', 'placeholder': 'Bachelor of Science in Computer Science'}),

            'skills': forms.Textarea(attrs={'class': 'field-control', 'rows': 4, 'placeholder': 'Project management, Python, Django, data analysis'}),
            'work_experience': forms.Textarea(attrs={'class': 'field-control', 'rows': 4, 'placeholder': 'Senior Developer at Company, delivered X, improved Y'}),
            'projects': forms.Textarea(attrs={'class': 'field-control', 'rows': 4, 'placeholder': 'Resume generator, website redesign, automation script'}),
            'certifications': forms.Textarea(attrs={'class': 'field-control', 'rows': 3, 'placeholder': 'AWS Certified, Scrum Master, etc.'}),
            'languages': forms.TextInput(attrs={'class': 'field-control', 'placeholder': 'English, French, Spanish'}),

            'linkedin_profile': forms.URLInput(attrs={'class': 'field-control', 'placeholder': 'https://linkedin.com/in/yourname'}),
            'github_profile': forms.URLInput(attrs={'class': 'field-control', 'placeholder': 'https://github.com/yourname'}),
            'portfolio_website': forms.URLInput(attrs={'class': 'field-control', 'placeholder': 'https://yourportfolio.com'}),
            'passport_photo': forms.FileInput(attrs={'class': 'field-control'}),
        }