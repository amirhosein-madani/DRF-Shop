from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Product(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    description = models.TextField()
    category = models.ManyToManyField("Category")
    price = models.DecimalField(max_digits=6, decimal_places=3)
    slug = models.SlugField(blank=True, unique=True)
    color = models.ManyToManyField("Color", blank=True)
    size = models.ManyToManyField("Size", blank=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})
