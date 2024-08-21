import factory  # Correct import for factory_boy
from .models import Product

class ProductFactory(factory.django.DjangoModelFactory):
    # Meta class to specify model information for the factory
    class Meta:
        # The model that this factory will create instances of
        model = Product

    # The name of the product is generated using the Faker library to create a random company name
    name = factory.Faker('company')

    # The price of the product is generated as a random integer between 200 and 9000 using Faker
    price = factory.Faker('random_int', min=200, max=9000)
