from django.shortcuts import render
from .forms import reservationForm


# Create your views here.

def reserve(request):
    reserve_form = reservationForm()
    if request.method == "POST":
        reserve_form = reservationForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = reservationForm()

    context = {
        "form":reserve_form,
    }

    return render (request,"reservation/reservation.html",context)