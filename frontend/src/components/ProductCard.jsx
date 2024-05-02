import { Card } from 'react-bootstrap';

const ProductCard = (props) => {
    const { name, price } = props.product

    return <Card>
        <Card.Img variant="top" src="placeholder-image.jpg" style = {{ height: '200px'}} />
        <Card.Body>
            <Card.Title>{name}</Card.Title>
            <Card.Text>
                £{price.toFixed(2)}
            </Card.Text>
        </Card.Body>
    </Card>
}

export default ProductCard;