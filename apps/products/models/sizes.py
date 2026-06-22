from django.db import models
from django.urls import reverse


class Size(models.Model):
    """
    this is a model for ProdcutModel's sizes
    """

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("size-detail", kwargs={"pk": self.pk})
