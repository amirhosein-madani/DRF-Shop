
import json
from django.core.cache import cache


class Cart:

    def __init__(self, user_id):
        self.user_id = user_id
        self.key = f"cart_{user_id}"
        self.cart = self._get_cart()

    def _get_cart(self):
        cart = cache.get(self.key)
        if not cart:
            return {}
        return cart

    def add(self, product_id, quantity, price):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id]["quantity"] += quantity
        else:
            self.cart[product_id] = {"quantity": quantity, "price": str(price)}
        self._save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self._save()

    def clear(self):
        cache.delete(self.key)
        self.cart = {}

    def _save(self):
        cache.set(self.key, self.cart, timeout=60 * 60 * 24 * 7)

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            float(item["price"]) * item["quantity"] for item in self.cart.values()
        )
