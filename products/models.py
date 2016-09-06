from django.db import models

# Creating our product models
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    #slug
    #inventory?

    # Product Images

    # Product Categories
