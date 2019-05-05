from django import forms
from .models import Schedule

class PostForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = {'schedule_date','title', 'memo',}