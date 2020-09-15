from django.forms import ModelForm

from auctions.models import Listing, Comment


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        exclude = ['created_by', 'is_closed']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['placed_by', 'placed_at', 'listing']
