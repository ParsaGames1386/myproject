
from django.urls import path
from .views import (ProductListView,ProductDetailView,CategoryDetailView,CategoryListView,FileListView,FileDetailView


                    )

urlpatterns = [
    path('products/',ProductListView.as_view(),name='products-list'),
    path('products/<int:pk>',ProductDetailView.as_view(),name='product-detail'),
    path('products/<int:product_pk>/files/',FileListView.as_view(),name='files-list'),
path(
    'products/<int:product_pk>/files/<int:pk>/',
    FileDetailView.as_view(),
    name='file-detail'
),


    path('categories/',CategoryListView.as_view(),name='categories-list'),
    path('categories/<int:pk>',CategoryDetailView.as_view(),name='category-detail'),
]
