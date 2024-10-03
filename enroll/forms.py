from django import forms
from .models import Enrolled

class EnrolledForm(forms.ModelForm):
    class Meta:
        model = Enrolled
        fields = ['course_name', 'enroll_by', 'course_module', 'payment_method', 'payment_date']
