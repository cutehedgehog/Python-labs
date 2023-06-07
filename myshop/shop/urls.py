from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='list_products'),
    path('<int:id>',views.product_details, name='product_details'),
    path('<str:product_provider_name>/', views.product_list,
         name='list_products_by_provider'
         ),
]
