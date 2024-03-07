from django.db import models

# Create your models here.

class Product(models.Model):
    img = models.ImageField(
        blank=True,
        upload_to="products / "
        
    )
    title = models.CharField(
        max_length=256
    )
    description = models.TextField()
    price = models.FloatField()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product"
    
    def __str__(self) -> str:
        return self.title
