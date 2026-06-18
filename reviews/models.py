from django.db import models
from products.models.products import Product

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    reply = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if self.pk:
            self.is_active = False
        super().save(*args, **kwargs)
