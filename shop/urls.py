from django.urls import path
from .views import ShopView, ProductDitailView


app_name = 'shop'

urlpatterns = [
    path('', ShopView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDitailView.as_view(), name='detail')
]