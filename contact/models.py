from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Contact(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=70)
    email = models.EmailField(_("آدرس الکترونیکی"), max_length=254)
    title = models.CharField(_("عنوان"), max_length=50)
    message = models.CharField(_("پیغام"), max_length=500)