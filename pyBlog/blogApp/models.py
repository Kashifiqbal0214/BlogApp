from django.db import models

# Create your models here.
class BlogTable(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    post = models.CharField(max_length=255)
    post_date = models.DateField(null= True)

    def __str__(self):
        return f"{self.name}"
    
    

