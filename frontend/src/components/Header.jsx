import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';
import { NavLink } from 'react-router-dom';

const Header = () => {
    return (
        <Navbar bg="dark" variant="dark" expand="lg" sticky="top">
            <Container>
                <Navbar.Brand as={NavLink} to="/">Edgar's Online Store</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="me-auto">
                    <Nav.Link as={NavLink} to='/products'>Products</Nav.Link>
                    <Nav.Link as={NavLink} to='/products/new'>Add a Product</Nav.Link>
                </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
};

export default Header;