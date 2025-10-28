import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div style={{ textAlign: 'center', padding: '2rem' }}>
      <h1>Bienvenue sur notre site !</h1>
      <p>Découvrez notre catalogue de produits.</p>
      <Link to="/catalogue" style={{ color: 'neon', fontSize: '1.5rem' }}>
        Voir le catalogue
      </Link>
    </div>
  );
};

export default HomePage;