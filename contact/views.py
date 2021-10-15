from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
    else:
        contact_form = ContactForm()

    context = {
        "contact" : contact_form,
    }    

    return render (request,"contact.html",context)     