from django.core.management.base import BaseCommand
from faker import Faker
from random import choice
from ...models.categories import Category
from ...models.colors import Color
from ...models.products import Product


class Command(BaseCommand):
    help = "creating random users and posts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):

        categories = list(Category.objects.all())
        colors = list(Color.objects.all())

        for _ in range(10):
            product = Product.objects.create(
                title=self.fake.word(),
                description=self.fake.paragraph(nb_sentences=10),
                price=self.fake.numerify("###"),
                stock=self.fake.numerify("##"),
            )

            product.category.add(choice(categories))
            product.color.add(choice(colors))
