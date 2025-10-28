import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

interface Produit {
  id: number;
  nom: string;
  description: string;
  prix: number;
  image: string;
}

const ProductDetailPage = () => {
  const { id } = useParams<{ id: string }>();
  const [produit, setProduit] = useState<Produit | null>(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/api/produits/${id}/`)
      .then(response => setProduit(response.data))
      .catch(error => console.error('Erreur lors du chargement du produit:', error));
  }, [id]);

  if (!produit) {
    return <p>Chargement...</p>;
  }

  return (
    <div style={{ padding: '2rem' }}>
      <h1>{produit.nom}</h1>
      <img src={produit.image} alt={produit.nom} style={{ maxWidth: '300px' }} />
      <p>{produit.description}</p>
      <p>Prix: {produit.prix}€</p>
    </div>
  );
};

export default ProductDetailPage;