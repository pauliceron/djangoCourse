from django.db import models

# Create your models here.

class Product(models.Model):
    # The name of the product, stored as a character field with a maximum length of 255 characters.
    name = models.CharField(max_length=255)
    
    # The price of the product, stored as an integer (in cents or units).
    price = models.IntegerField()
    
    # The date and time when the product was created, automatically set when the object is first created.
    created_at = models.DateTimeField(auto_now_add=True)
    
    # The date and time when the product was last updated, automatically updated whenever the object is saved.
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 description = models.TextField()