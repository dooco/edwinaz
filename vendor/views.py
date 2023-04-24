from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from .models import Vendor


def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.Post)

        if form.is_valid():
            user = form.save()
            login(request, user)
            vendor = Vendor.objects.create(name=user.username, created_by=user)
            return redirect('home')
    else:
        form = UserCreationForm()
    template = 'vendor/become_vendor.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def vendor(request):
    vendor = request.user.vendor
    template = 'vendor/vendor.html'
    context = {
        'vendor': vendor
    }

    return render(request, template, context)

