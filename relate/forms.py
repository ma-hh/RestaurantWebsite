from django import forms
from .models import Relate

class RelateForm(forms.ModelForm):

    class Meta:
        model = Relate
        fields = "__all__"
