from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Relate(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=50)
    email = models.EmailField(_("آدرس الکترونیکی"), max_length=254)
    title = models.CharField(_("عنوان"), max_length=50)
    message = models.CharField(_("پیغام"), max_length=400)

    def __str__(self):
        return self.title
    