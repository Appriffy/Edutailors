from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    votes = models.IntegerField(null=True)
    submitterAvatarUrl = models.ImageField(default="default.png",upload_to="avatar", blank=True)
    productImageUrl = models.ImageField(default="default.png",upload_to='product',blank=True)

    def __str__(self):
        return self.title
