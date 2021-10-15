from django.urls import path
from . import views

app_name = "relate"
urlpatterns = [
    path('',views.relator,name="contactus")
]

