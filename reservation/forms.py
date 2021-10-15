from django import forms
from .models import reservation

class reservationForm(forms.ModelForm):
    
    class Meta:
        model = reservation
        fields = "__all__"

    

