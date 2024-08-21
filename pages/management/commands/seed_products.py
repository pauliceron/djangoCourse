from django.core.management.base import BaseCommand
from pages.factories import ProductFactory

class Command(BaseCommand):
    # Help text that provides a description of what the command does.
    help = 'Seed the database with products'

    # The handle method is called when the custom command is executed.
    def handle(self, *args, **kwargs):
        # Create a batch of 8 product instances using the ProductFactory.
        ProductFactory.create_batch(8)

        # Output a success message to the console once the products are seeded.
        self.stdout.write(self.style.SUCCESS('Successfully seeded products'))