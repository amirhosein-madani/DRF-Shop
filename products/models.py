from django.db import models
from django.utils.text import slugify
# Create your models here.

class Products(models.Model):
    
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    description = models.TextField()
    category = models.ManyToManyField('Category')
    price = models.DecimalField( max_digits=6,decimal_places=3)
    slug = models.SlugField(blank= True , unique= True)
    color = models.ManyToManyField('Color', blank=True)
    size = models.ManyToManyField('Size', blank=True)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Products.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    image = models.ImageField(upload_to="product_categories", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "Categories"


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name