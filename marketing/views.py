from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from marketing.forms import EmailForm
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import hashlib


mailchimp = Client()
mailchimp.set_config({
  'api_key': settings.MAILCHIMP_API_KEY,
  'server': settings.MAILCHIMP_REGION,
})

def subscribe_view(request):
    """ A view to suscribe to mailchimp page """
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                member_info = {
                    'email_address': form_email,
                    'status': 'subscribed',
                }
                response = mailchimp.lists.add_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    member_info,
                )
                messages.success(request, 'Successfully Suscribed!')

                return redirect('subscribe-success')

            except ApiClientError as error:
                messages.error(request, 'An exception occurred.')
                return redirect('subscribe-fail')

    return render(request, 'marketing/subscribe.html', {
        'form': EmailForm(),
    })


def subscribe_success_view(request):
    """ Suscribe success view """
    messages.success(request, 'Successfully subscribed to our mailing list')
    return redirect(reverse('products'))


def subscribe_fail_view(request):
    """ Suscribe fail view """
    messages.error(request,
                   ('Failed to subscribe. Please ensure the form is valid.'))
    return redirect(reverse('subscribe'))


def unsubscribe_view(request):
    """ A view to unsuscribe to mailchimp page """
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                form_email_hash = hashlib.md5(form_email.encode('utf-8').lower()).hexdigest()
                member_update = {
                    'status': 'unsubscribed',
                }
                response = mailchimp.lists.update_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    form_email_hash,
                    member_update,
                )
                messages.success(request, 'Successfully Un-suscribed!')
                return redirect('unsubscribe-success')
            except ApiClientError as error:
                messages.error(request,
                   ('Exception occured.'))
                return redirect('unsubscribe-fail')

    return render(request, 'marketing/unsubscribe.html', {
        'form': EmailForm(),
    })


def unsubscribe_success_view(request):
    """ Unsuscribe success view """
    messages.success(request, 'Successfully un-subscribed from our mailing list')
    return redirect(reverse('products'))


def unsubscribe_fail_view(request):
    """ Unsuscribe fail view """
    messages.error(request,
                   ('Failed to un-subscribe. Please ensure the form is valid.'))
    return redirect(reverse('unsubscribe'))