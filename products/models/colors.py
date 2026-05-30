from django.db import models
from django.urls import reverse


class Color(models.Model):
    """
    this is a model for producProdcutModelts's colors
    """

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("color-detail", kwargs={"pk": self.pk})
