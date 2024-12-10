from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
     taskAssignDate = forms.DateField(
        input_formats=['%d-%b-%Y', '%Y-%m-%d'],  # Accept formats like '08-Dec-2023' or '2023-12-08'
        widget=forms.DateInput(attrs={'placeholder': 'DD-MMM-YYYY'})  # Add a placeholder for user clarity
    )
     
     class Meta:
        model = TaskModel
        fields = '__all__'
