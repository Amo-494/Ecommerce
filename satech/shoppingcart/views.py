from lib2to3.pgen2 import token
from multiprocessing import context
from pyexpat.errors import messages
from time import timezone
from django.shortcuts import render, redirect

from shoppingcart.forms import CouponForm
from .models import *
from django.http import JsonResponse
import json
from .forms import CouponForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0}
        cartItems = order['get_cart_items', 'get_cart_items':0]

    # couponform = CouponForm()
    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'couponform': CouponForm()}
    return render(request, 'cart.html', context)


def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantty <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        # messages.info(request, "This coupon does not exist")
        print("This coupon does not exist")
        return redirect("cart")


def add_coupon(request):
    if request.method == "POST":
        form = CouponForm(request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(customer=request.user.customer, complete=False)
                coupon = Coupon.objects.get(code=code)
                # order.coupon = Coupon.objects.get(code=code)
                order.coupon = get_coupon(request,code)
                order.save()
                
                Order.get_cart_total()
                discount = 10
                discounted_price = total * discount/100
                total -= discounted_price
                    # return total
                
                context={'discounted_price':discounted_price,'total':total}
                # messages.success(request, "This coupon does not exist")
                print("Successfully added coupon")
                return redirect("cart",context)
            except ObjectDoesNotExist:
                # messages.info(request, "You do not have an active order")
                print("This coupon does not exist")
                return redirect("cart")
    return None
# def coupon_apply(request):
#     # now = timezone.now()
#     form = CouponApplyForm(request.POST)
#     if form.is_valid():
#         code = form.cleaned_data['code']
#         try:
#             coupon = Coupon.objects.get(code__iexact=code,active=True)

#             request.session['coupon_id'] = coupon.id
#         except Coupon.DoesNotExist:
#             request.session['coupon_id'] = None
#     return redirect('cart:cart_detail')
