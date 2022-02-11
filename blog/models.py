from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    description=models.TextField(max_length=500)
    image=models.ImageField(upload_to='blog/images/')
    url=models.URLField(blank=True)
    
    def __str__(self):
        return self.title