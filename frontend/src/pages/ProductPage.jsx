import { useEffect, useState } from "react";
import axios from 'axios';

const ProductPage = () => {
    const [ products, setProducts ] = useState([]);
    const [ loading, setLoading ] = useState(true);
    const [ error, setError ] = useState(null);
    
    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get('http://localhost:5000/products');
                setProducts(response.data.products);
                console.log(response.data.products);
            } catch(err) {
                setError(err.message || 'An error occurred');
            } finally {
                setLoading(false);
            }
        }

        fetchProducts();
    }, [])

    if (loading) return <div>Loading...</div>
    if (error) return <div>Error: {error}</div>

    return (
        <div>
          <h1>Products</h1>
          <ul>
            {products.map(product => (
              <li key={product.id}>
                {product.name} - ${product.price}
              </li>
            ))}
          </ul>
        </div>
      );
}

export default ProductPage;