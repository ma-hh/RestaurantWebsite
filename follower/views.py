from django.shortcuts import render
from .forms import FollowersForm

# Create your views here.

def follow(request):
    followers_form = FollowersForm()
    if request.method == "POST":
        followers_form = FollowersForm(request.POST)
        if followers_form.is_valid():
            followers_form.save()
    else:
        followers_form = FollowersForm()

    context={
        "formf" : followers_form,
    }
    
    return render(request,'__footer.html',context)