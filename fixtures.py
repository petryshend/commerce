from django.contrib.auth import get_user_model
from auctions.models import Category, Listing

lorem = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur aut beatae consequuntur corporis cum earum eius excepturi exercitationem facere illum iure laboriosam nostrum officia officiis repudiandae soluta tempora, tempore, voluptates.'

# Users
User = get_user_model()
admin = User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')
user = User.objects.create_user('user', 'user@user.com', 'user')


# Categories
for cat_name in ['Fashion', 'Toys', 'Electronics', 'Home']:
    category = Category(name=cat_name)
    category.save()

# Listings
l1 = Listing(title='First listing', description=lorem, starting_bid=10, created_by=admin)
l1.save()
category = Category.objects.get(name='Home')
l2 = Listing(title='Second listing', description=lorem, starting_bid=10, image_url='http://lorempixel.com/400/400/', category=category, created_by=admin)
l2.save()
l3 = Listing(title='Third listing', description=lorem, starting_bid=20, image_url='http://lorempixel.com/400/400/', category=category, created_by=admin)
l3.save()

