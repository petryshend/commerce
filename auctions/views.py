from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import User, Listing, Watchlist, Bid, Comment
from auctions.forms import ListingForm, CommentForm


def index(request):
    return render(request, "auctions/index.html", {
        'listings': Listing.objects.all().order_by('-id')
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        listing = form.save(commit=False)
        listing.created_by = request.user
        listing.save()
        return redirect(reverse('index'))
    form = ListingForm()
    return render(request, 'auctions/create_listing.html', {
        'form': form
    })


def view_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    in_watchlist = False
    if request.user.is_authenticated:
        try:
            watchlist = Watchlist.objects.get(user=request.user)
            for l in watchlist.listings.all():
                if l.id == listing_id:
                    in_watchlist = True
        except Watchlist.DoesNotExist:
            pass

    current_bids = Bid.objects.filter(listing=Listing.objects.get(pk=listing_id))
    latest_bid = None
    if current_bids:
        latest_bid = current_bids.order_by('-amount')[0]

    if latest_bid:
        min_bid = latest_bid.amount + 1
    else:
        min_bid = listing.starting_bid + 1

    return render(request, 'auctions/view_listing.html', {
        'listing': listing,
        'in_watchlist': in_watchlist,
        'current_bids_count': len(current_bids),
        'latest_bid': latest_bid,
        'min_bid': min_bid,
        'comments': Comment.objects.filter(listing=listing).order_by('-placed_at'),
        'comment_form': CommentForm()
    })


@login_required
def add_to_watchlist(request, listing_id):
    if request.method != 'POST':
        return redirect(reverse('view_listing', args=[listing_id]))
    try:
        watchlist = Watchlist.objects.get(user=request.user)
    except Watchlist.DoesNotExist:
        watchlist = Watchlist(user=request.user)
        watchlist.save()
    listing = Listing.objects.get(pk=listing_id)
    watchlist.listings.add(listing)
    return redirect(reverse('view_listing', args=[listing_id]))


@login_required
def remove_from_watchlist(request, listing_id):
    if request.method != 'POST':
        return redirect(reverse('view_listing', args=[listing_id]))
    watchlist = Watchlist.objects.get(user=request.user)
    watchlist.listings.remove(Listing.objects.get(pk=listing_id))
    return redirect(reverse('view_listing', args=[listing_id]))


@login_required
def place_bid(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.method != 'POST':
        return redirect(reverse('view_listing', args=[listing_id]))
    latest_bid = Bid.objects.filter(listing=Listing.objects.get(pk=listing_id)).order_by('-amount').first()
    if latest_bid:
        min_bid_amount = latest_bid.amount
    else:
        min_bid_amount = listing.starting_bid
    current_bid = float(request.POST['bid'])
    if min_bid_amount > current_bid:
        messages.add_message(request, messages.ERROR, 'Your bid should be greater than latest bid')
        return redirect(reverse('view_listing', args=[listing_id]))

    new_bid = Bid(amount=current_bid, listing=listing, placed_by=request.user)
    new_bid.save()
    messages.add_message(request, messages.INFO, 'You successfully placed new bid')
    return redirect(reverse('view_listing', args=[listing_id]))


@login_required
def close_listing(request, listing_id):
    if request.method != 'POST':
        return redirect(reverse('view_listing', args=[listing_id]))
    listing = Listing.objects.get(pk=listing_id)
    listing.is_closed = True
    listing.save()
    messages.add_message(request, messages.INFO, 'You closed this listing')
    return redirect(reverse('view_listing', args=[listing_id]))


@login_required
def add_comment(request, listing_id):
    if request.method != 'POST':
        return redirect(reverse('view_listing', args=[listing_id]))
    listing = Listing.objects.get(pk=listing_id)
    form = CommentForm(request.POST)
    comment = form.save(commit=False)
    comment.placed_by = request.user
    comment.listing = listing
    comment.save()
    return redirect(reverse('view_listing', args=[listing_id]))


@login_required
def view_watchlist(request):
    try:
        watchlist = Watchlist.objects.get(user=request.user)
        listings = watchlist.listings.filter(is_closed=False)
    except Watchlist.DoesNotExist:
        listings = []
    return render(request, "auctions/index.html", {
        'listings': listings
    })