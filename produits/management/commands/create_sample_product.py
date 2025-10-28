from django.core.management.base import BaseCommand
from produits.models import Produit

class Command(BaseCommand):
    help = 'Créer des produits exemples dans la base de données'

    def handle(self, *args, **kwargs):
        produits = [
            {
                'nom': 'Roccat CLAVIER',
                'description': 'Un clavier mécanique avec un design RGB.',
                'prix': 99.99,
                'image': 'https://media.ldlc.com/r705/ld/products/00/06/09/70/LD0006097031.jpg',
                'categorie': 'Accessoires'
            },
            {
                'nom': 'Neon Mouse',
                'description': 'Une souris RGB avec des effets lumineux.',
                'prix': 49.99,
                'image': '',
                'categorie': 'Accessoires'
            },
            {
                'nom': 'Holo Monitor',
                'description': 'Un écran holographique dernière génération.',
                'prix': 299.99,
                'image': '',
                'categorie': 'Électronique'
            },
            {
                'nom': 'The Witcher Chair',
                'description': 'Une chaise gaming avec un style The Witcher.',
                'prix': 199.99,
                'image': '',
                'categorie': 'Mobilier'
            }
        ]

        for produit_data in produits:
            produit, created = Produit.objects.get_or_create(**produit_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Produit créé : {produit.nom}'))
            else:
                self.stdout.write(self.style.WARNING(f'Produit existant : {produit.nom}'))

Produit.objects.all().delete()