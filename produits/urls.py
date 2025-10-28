from django.urls import path
from .views import ProduitListAPIView, ProduitDetailAPIView

urlpatterns = [
    path('produits/', ProduitListAPIView.as_view(), name='produit-list'),
    path('produits/<int:pk>/', ProduitDetailAPIView.as_view(), name='produit-detail'),
]
