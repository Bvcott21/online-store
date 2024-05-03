import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from 'axios';
import { Button, ButtonGroup, Card, Col, Container, Row } from "react-bootstrap";

const ProductDetailsPage = () => {
    const { id } = useParams();
    const navigate = useNavigate();

    const [ product, setProduct ] = useState({});
    const [ loading, setLoading ] = useState(true);
    const [ error, setError ] = useState(null);

    const handleBackToAllProductsPageClick = () => {
        navigate('/products')
    }

    useEffect(() => {
        const fetchProduct = async () => {
            try {
                const response = await axios.get('http://localhost:5000/products/'+id);
                setProduct(response.data.product);
                console.log(response.data)
            } catch(err) {
                setError(err.message || 'An error occurred');
            } finally {
                setLoading(false);
            }
        }
        fetchProduct();
    }, [id])

    if (loading) return <div>Loading...</div>
    if (error) return <div>Error: {error}</div>

    return (
        <Container>
            <Row className="justify-content-center mt-5">
                <Col md={6}>
                    <Card>
                        <Card.Body>
                            <Card.Title>{product.name}</Card.Title>
                            <Card.Subtitle className="mb-2 text-muted">
                                Price: £{product.price.toFixed(2)}
                            </Card.Subtitle>
                            <Card.Text>
                                <strong>Description:</strong> {product.description}
                            </Card.Text>
                            <Card.Text>
                                <strong>Category:</strong> {product.categories.join(', ')}
                            </Card.Text>
                            {
                                product.discontinued && (
                                    <Card.Text className="text-danger">
                                        This product has been discontinued.
                                    </Card.Text>
                                )
                            }
                            <ButtonGroup className=''>
                                <Button variant="primary" disabled={product.discontinued}>
                                    {product.discontinued ? 'Unavailable' : 'Add to Cart'}
                                </Button>
                                <Button onClick={handleBackToAllProductsPageClick}>
                                    Keep Browsing
                                </Button>
                            </ButtonGroup>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>

    )
}

export default ProductDetailsPage;