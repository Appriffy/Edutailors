from django.shortcuts import render
from django.http import Http404, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

from .models import Product


def home(request):
    prods = Product.objects.all()
    return render(request, 'home.html', {'prods': prods})


# def product_detail(request, id=1):
#     try:
#         prod = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         raise Http404("Product not found")
#     return render(request, 'product_detail.html', {'prod': prod})


@api_view(['GET'])
def product_all(request):
    if request.method == 'GET':
        data = []
        products = Product.objects.all().order_by('-votes')
        # products = Product.objects.all()
        for product in products:
            payload = {"id": product.id, "title": product.title, "description": product.description,
                       "votes": product.votes, "submitterAvatarUrl": "media/" + str(product.submitterAvatarUrl),
                       "productImageUrl": "media/" + str(product.productImageUrl)}
            data.append(payload)
    return Response({"response": data})


from django.views.decorators.csrf import csrf_exempt


@api_view(['PUT'])
def num_update(request, pk):
    if request.method == 'PUT':
        data = request.data
        product = Product.objects.get(pk=pk)
        product.votes = int(data['votes'])
        product.save()
    return Response({"status": "okk"})
