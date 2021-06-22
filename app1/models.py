from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Blog(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=5000)
    author=models.CharField(max_length=30)
    publised_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title