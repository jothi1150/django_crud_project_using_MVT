
from django import forms
from .models import StudentData


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentData

        fields = [
            'name',
            'gender',
            'dob',
            'phone',
            'email',
            'department',
            'course',
            'city',
            'address',
        ]

        widgets = {
            'dob': forms.DateInput(attrs={
                'type': 'date'
            }),

            'address': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Enter your full address'
            }),

            'name': forms.TextInput(attrs={
                'placeholder': 'Enter student name'
            }),

            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter phone number'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email address'
            }),

            'department': forms.TextInput(attrs={
                'placeholder': 'Enter department'
            }),

            'course': forms.TextInput(attrs={
                'placeholder': 'Enter course'
            }),

            'city': forms.TextInput(attrs={
                'placeholder': 'Enter city'
            }),
        }
