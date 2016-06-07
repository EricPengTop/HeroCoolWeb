from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.context import RequestContext
from django.template.loader import get_template

from ShopApp.forms import ProductForm
from ShopApp.models import Product


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    t = get_template('shopapp/create_product.html')
    c = RequestContext(request.locals())
    return HttpResponse(t.render(c))


def list_product(request):
    list_items = Product.objects.all()
    paginator = Paginator(list_items, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except:
        list_items = paginator.page(paginator.num_pages)

    t = get_template('shopapp/product_list.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def view_product(request, id):
    product_instane = Product.objects.get(id=id)
    t = get_template('shopapp/view_product.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def edit_product(request, id):
    product_instance = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product_instance)
    if form.is_valid():
        form.save()
    t = get_template('shopapp/edit_product.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))
