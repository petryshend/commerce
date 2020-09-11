from django.contrib.auth import get_user_model
from auctions.models import Category, Listing

# Users
User = get_user_model()
user = User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')

# Categories
for cat_name in ['Fashion', 'Toys', 'Electronics', 'Home']:
    category = Category(name=cat_name)
    category.save()

# Listings
lorem = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur aut beatae consequuntur corporis cum earum eius excepturi exercitationem facere illum iure laboriosam nostrum officia officiis repudiandae soluta tempora, tempore, voluptates.'
l1 = Listing(title='First listing', description=lorem, starting_bid=10)
l1.save()
category = Category.objects.get(name='Home')
l2 = Listing(title='Second listing', description=lorem, starting_bid=10, image_url='http://lorempixel.com/400/400/', category=category)
l2.save()
l3 = Listing(title='Third listing', description=lorem, starting_bid=20, image_url='http://lorempixel.com/400/400/', category=category)
l3.save()

