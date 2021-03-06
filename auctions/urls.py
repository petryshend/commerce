from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('listing/create', views.create_listing, name='create_listing'),
    path('listing/watchlist', views.view_watchlist, name='view_watchlist'),
    path('listing/categories', views.view_categories, name='view_categories'),
    path('listing/<int:listing_id>', views.view_listing, name='view_listing'),
    path('listing/<int:listing_id>/add-to-watchlist', views.add_to_watchlist, name='add_to_watchlist'),
    path('listing/<int:listing_id>/remove-from-watchlist', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('listing/<int:listing_id>/place-bid', views.place_bid, name='place_bid'),
    path('listing/<int:listing_id>/close-listing', views.close_listing, name='close_listing'),
    path('listing/<int:listing_id>/add-comment', views.add_comment, name='add_comment')
]
