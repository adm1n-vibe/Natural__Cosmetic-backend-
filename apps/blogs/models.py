from django.db import models

class Blog (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField (max_length= 256)
    img = models.ImageField(blank=True, null=True)
    upload = models.BooleanField(default=0)

    class Meta:
        verbose_name = ('Blog')
        verbose_name_plural = ('Blogs')
        # ordering = ['-id']

      
