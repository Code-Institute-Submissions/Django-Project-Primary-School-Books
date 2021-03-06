from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def all_products(request):
    product_list = Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})


def product_info(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, "product-info.html", {'product': product})
