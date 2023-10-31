from django import forms
from .models import TimeOffRequest

class TimeOffRequestForm(forms.ModelForm):
    class Meta:
        model = TimeOffRequest
        fields = ['request_type', 'start_date', 'end_date', 'reason','user', 'status']
        exclude = ['created_at', 'updated_at']
    
