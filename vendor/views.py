from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm
from .models import Vendor
from products.models import Product
from products.forms import ProductForm

from profiles.models import UserProfile
from profiles.forms import UserProfileForm

from checkout.models import Order

@login_required
def vendor(request):
    """ A view to return the vendor page """
    
    products = Product.objects.filter(user=request.user)
   
    template = 'vendor/vendor.html'

    context = {
        'vendor': vendor,
        'products': products,
    }

    return render(request, template, context)


@login_required
def become_vendor_OLD(request):
    """ Become a vendor OLD """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save(commit=False)
            form.userprofile.is_vendor = True
            form.save()
            print(userprofile)
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                        ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)

    template = 'vendor/become_vendor.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)

@login_required
def become_a_vendor(request):
    """ Become a vendor """

    profile = get_object_or_404(UserProfile, user=request.user)
    profile.is_vendor = 'True'
    profile.save()
    context = {
        'UserProfile': profile
    }
    template = 'vendor/become_a_vendor.html'
    
    return render(request, template, context)

def vendor_product_detail(request, product_id):
    """ A view to show individual vendor's product details """

    product = get_object_or_404(Product, pk=product_id)
    template = 'vendor/vendor_product_detail.html'

    context = {
        'product': product,
    }

    return render(request, template, context)


@login_required
def vendor_add_product(request):
    """ Add a product to the store """
    if not request.user.userprofile.is_vendor:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'vendor/vendor_add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def vendor_edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.userprofile.is_vendor:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'vendor/vendor_edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def vendor_delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.userprofile.is_vendor:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('vendor'))

