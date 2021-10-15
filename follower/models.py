from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Followers(models.Model):
    email = models.EmailField(_("آدرس الکترونیکی"), max_length=254)

    def __str__(self):
        return self.email
    