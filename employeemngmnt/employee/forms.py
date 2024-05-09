from django import forms
from .models import Department,Employee

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields="__all__"

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"