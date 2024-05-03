import { useEffect, useState } from "react";
import axios from 'axios';
import { Container, Row, Col } from "react-bootstrap";
import ProductCard from "../components/ProductCard";
import ReactPaginate from 'react-paginate';
import { Link } from "react-router-dom";

const ProductPage = () => {
    const [ products, setProducts ] = useState([]);
    const [ loading, setLoading ] = useState(true);
    const [ error, setError ] = useState(null);
    const [ currentPage, setCurrentPage ] = useState(0);
    
    // Constants for pagination
    const PRODUCTS_PER_PAGE = 25;
    const pageCount = Math.ceil(products.length / PRODUCTS_PER_PAGE);

    // Function to handle page click
    const handlePageClick = (selectedItem) => {
      setCurrentPage(selectedItem.selected)
    }

    // Get current products to display
    const currentProducts = products.slice(
      currentPage * PRODUCTS_PER_PAGE,
      (currentPage + 1) * PRODUCTS_PER_PAGE 
    );

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get('http://localhost:5000/products');
                setProducts(response.data.products);
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
        <Container>
          <h1 className="my-5">All products</h1>
          <Row xs={1} md={2} lg={5} className="g-4">
            {currentProducts.map((product) => (
              <Col key={product.id}>
                <Link to={`/products/${product.id}`} style={{textDecoration: 'none'}}>
                <ProductCard product={product} />
                </Link>
              </Col>
            ))}
          </Row>
          <ReactPaginate
            previousLabel={'Previous'}
            nextLabel={'Next'}
            breakLabel={'...'}
            pageCount={pageCount}
            marginPagesDisplayed={2}
            pageRangeDisplayed={5}
            onPageChange={handlePageClick}
            containerClassName={'pagination justify-content-center mt-5'}
            pageClassName={'page-item'}
            pageLinkClassName={'page-link'}
            previousClassName={'page-item'}
            previousLinkClassName={'page-link'}
            nextClassName={'page-item'}
            nextLinkClassName={'page-link'}
            breakClassName={'page-item'}
            breakLinkClassName={'page-link'}
            activeClassName={'active'}
          />
        </Container>
      );
}

export default ProductPage;