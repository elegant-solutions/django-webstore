from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

from products.models import Product
from .forms import SignUpForm
from .models import SignUp


def home(request):
    title = 'Sign Up Now'

    products = Product.objects.all()
    form = SignUpForm(request.POST or None)
    context = {
        'title': title,
        'form': form,
        'products': products
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank you"
        }

    if request.user.is_authenticated() and request.user:
        print(SignUp.objects.all())
        queryset = SignUp.objects.all().order_by('-timestamp')
        context = {
          "queryset": queryset
        }

    return render(request, 'home.html', context)
