from django import forms
from .models import Followers

class FollowersForm(forms.ModelForm):
    
    class meta():
        model = Followers
        fields = "__all__"