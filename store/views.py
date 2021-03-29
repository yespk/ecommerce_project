from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import BrandForm
from .models import Brand, Product


# Create your views here.
def index(request):
    brands = Brand.objects.all()
    products = Product.objects.all()
    return render(request, 'store/index.html', {'brands': brands, 'products': products})


def set_brands(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store:success')
    else:
        form = BrandForm()
    return render(request, 'store/addbrand.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded!!!')
