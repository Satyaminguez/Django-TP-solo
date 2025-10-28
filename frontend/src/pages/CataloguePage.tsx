import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

interface Produit {
  id: number;
  nom: string;
  prix: number;
}

const CataloguePage = () => {
  const [produits, setProduits] = useState<Produit[]>([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/produits/')
      .then(response => setProduits(response.data))
      .catch(error => console.error('Erreur lors du chargement des produits:', error));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Catalogue</h1>
      <ul>
        {produits.map(produit => (
          <li key={produit.id}>
            <Link to={`/produit/${produit.id}`} style={{ color: 'neon' }}>
              {produit.nom} - {produit.prix}€
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CataloguePage;