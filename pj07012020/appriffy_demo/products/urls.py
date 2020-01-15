from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    # re_path(r'(\d+)', views.product_detail, name='product_detail'),
    path("getall/", views.product_all),
    path("votes/<int:pk>", views.num_update)
]
