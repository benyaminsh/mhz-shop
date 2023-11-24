from django.urls import path
from . import views

app_name = 'app_products'

urlpatterns = [
    path('', views.ProductsView.as_view(), name='products'),
    path('retrieve/', views.ProductRetrieveView.as_view(), name='product_retrieve'),
    path('comment/create/', views.ProductCommentCreateView.as_view(), name='product_comment_create'),
]
