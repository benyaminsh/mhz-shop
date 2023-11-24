from django.urls import path
from . import views

app_name = 'app_managers'

urlpatterns = [
    # Products
    path('product/list_create/', views.ProductListCreateView.as_view(), name='product_list_create'),
    path('product/retrieve_update_destroy/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product_retrieve_update_destroy'),
    # Categories
    path('category/list_create/', views.CategoryListCreateView.as_view(), name='category_list_create'),
    path('category/retrieve_update_destroy/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category_retrieve_update_destroy'),
    # Features
    path('feature/list_create/', views.FeatureListCreateView.as_view(), name='feature_list_create'),
    path('feature/retrieve_update_destroy/', views.FeatureRetrieveUpdateDestroyView.as_view(), name='feature_retrieve_update_destroy'),
    # Comments
    path('comment/list/', views.CommentListView.as_view(), name='comment_list'),
    path('comment/retrieve_update_destroy/', views.CommentRetrieveUpdateDestroyView.as_view(), name='comment_retrieve_update_destroy'),
]
