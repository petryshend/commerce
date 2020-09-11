from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=False)
    starting_bid = models.DecimalField(max_digits=15, decimal_places=2)
    image_url = models.CharField(max_length=1024, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='listings')

    def __str__(self):
        return self.title


class Watchlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, unique=True)
    listings = models.ManyToManyField(Listing, blank=True, related_name='watchlists')

    def __str__(self):
        return f'Watchlist of {self.user.username}'
