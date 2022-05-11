from django.db import models
from django.conf import settings
# Notes
# __str__ defines the string output of the object when called with functions similar to print()
# The related_name attribute specifies the name of the reverse relation from the User model back to your model. Will return all the related instances
# on_delete=models.PROTECT protects the parent from deletion if a child exist in many-to-many or ForeignKey relations

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcateogories', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.TextField(max_length=500)
    text = models.TextField(max_length=5000)
    subcategory =  models.ForeignKey(SubCategory, related_name='articles', on_delete=models.PROTECT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='writings', on_delete=models.PROTECT)
    cover = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
