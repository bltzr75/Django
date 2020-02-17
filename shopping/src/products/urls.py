from django.conf.urls import url# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

from .views import product_list

app_name = 'products'

urlpatterns = [
    url(r'^', product_list, name='product-list')
]
