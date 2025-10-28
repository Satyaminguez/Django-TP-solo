from rest_framework import generics, filters
from .models import Produit
from .serializers import ProduitSerializer

# Liste des produits avec filtres (catégorie, prix min/max)
class ProduitListAPIView(generics.ListAPIView):
	queryset = Produit.objects.all()
	serializer_class = ProduitSerializer
	filter_backends = [filters.SearchFilter, filters.OrderingFilter]
	search_fields = ['nom', 'categorie']
	ordering_fields = ['prix']

	def get_queryset(self):
		queryset = super().get_queryset()
		categorie = self.request.query_params.get('categorie')
		prix_min = self.request.query_params.get('prix_min')
		prix_max = self.request.query_params.get('prix_max')
		if categorie:
			queryset = queryset.filter(categorie__iexact=categorie)
		if prix_min:
			queryset = queryset.filter(prix__gte=prix_min)
		if prix_max:
			queryset = queryset.filter(prix__lte=prix_max)
		return queryset

# Détail d'un produit
class ProduitDetailAPIView(generics.RetrieveAPIView):
	queryset = Produit.objects.all()
	serializer_class = ProduitSerializer
