from django.db import models

# Create your models here.
class Recipe(models.Model): #Name of the model is Recipe and it inherits models.Model)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    image = models.ImageField(upload_to="recipes/")
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

