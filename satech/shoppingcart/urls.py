# from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.store, name="store"),
    path('cart/',views.cart, name="cart"),
    path('update_item/',views.updateItem, name="update_item"),
    path('get_coupon/<code>/',views.get_coupon, name="get_coupon"),
    path('add_coupon/',views.add_coupon, name="add_coupon"),

]