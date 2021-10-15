from django.shortcuts import render
from .forms import RelateForm

# Create your views here.

def relator(request):
    relate_form = RelateForm()
    if request.method == "POST":
        relate_form = RelateForm(request.POST)
        if relate_form.is_valid():
                relate_form.save()
    else:
        relate_form = RelateForm()

    context ={
        "form":relate_form

    }
    return render(request,'relate/contact.html',context)


