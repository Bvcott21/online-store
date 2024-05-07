import React, { useState, useEffect } from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import { Form as RBForm, Container, Row, Col, Card } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';
import axios from 'axios';
import * as Yup from 'yup';

const AddProductForm = () => {

    const [ categories, setCategories ] = useState([]);

    useEffect(() => {
        axios
            .get('http://localhost:5000/categories')
            .then(response => {
                setCategories(response.data.categories);
            })
            .catch(err => {
                console.error('Error fetching categories: ' + err)
            })
    }, [])

    const productObjectMapper = (product) => {
        return {
            name: product.name,
            description: product.description,
            price: product.price,
            cost: product.cost,
            discontinued: false,
            current_stock: product.current_stock,
            category_ids: product.category_ids.join(",")
        }
    }
    
    return <Container className="justify-content-center align-items-center vh-100">
        <Row>
            <Col>
                <Card>
                    <Formik
                        initialValues={{
                            name:'',
                            description: '',
                            price: '',
                            cost: '',
                            current_stock: '',
                            discontinued: false,
                            category_ids: []
                        }}
                        validationSchema = {
                            Yup.object({
                                name: Yup.string().required('Required'),
                                description: Yup.string(),
                                price: Yup.number().min(0). required('Required'),
                                cost: Yup.number().min(0).required('Required'),
                                current_stock: Yup.number().min(0).required('Required'),
                                category_ids: Yup.array().of(Yup.string())
                            })
                        }
                        onSubmit = {(values, {setSubmitting, resetForm}) => {
                            const product = productObjectMapper(values)
                            axios
                                .post("http://localhost:5000/products", product, {
                                    headers: {
                                        "Content-Type": "application/json"
                                    }
                                })
                                .then(response => {
                                    console.log("Product added successfully:", response.data);
                                    resetForm();
                                })
                                .catch(err => {
                                    console.error("There was an error with product: ", err);
                                })
                                .finally(() => {
                                    setSubmitting(false);
                                })
                        }}
                    >
                {({
                    values,
                    errors,
                    touched,
                    handleChange,
                    handleBlur,
                    handleSubmit,
                    isSubmitting,
                    setFieldValue
                }) => (
                    <RBForm onSubmit={handleSubmit}>
                        <RBForm.Group className="mb-3">
                            <RBForm.Label>Name</RBForm.Label>
                            <RBForm.Control
                                type="text"
                                name="name"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.name}
                            />
                            {errors.name && touched.name && errors.name}
                        </RBForm.Group>



                        <RBForm.Group>
                            <RBForm.Label>Description</RBForm.Label>
                            <RBForm.Control
                                type="text"
                                name="description"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.description}
                            />
                            {errors.description && touched.description && errors.description}
                        </RBForm.Group>


                        
                        <RBForm.Group>
                            <RBForm.Label>Categories</RBForm.Label>
                            <RBForm.Control
                                as='select'
                                name="category_ids"
                                multiple
                                onChange={(e) => {
                                    const selectedOptions = Array.from(
                                        e.target.selectedOptions
                                    )
                                    .map(
                                        (option) => option.value
                                    );
                                    setFieldValue('category_ids', selectedOptions)
                                }}
                                onBlur={handleBlur}
                                value={values.category_ids}
                            >
                                {categories.length > 0 ? (
                                    categories.map((category) => (
                                        <option key={category.id} value={category.id}>
                                            {category.name}
                                        </option>
                                    ) 
                                )
                                ) : (
                                    <option disabled>No categories available</option>
                                )
                            } 
                            </RBForm.Control>
                            <RBForm.Text className="text-muted">
                                Hold Ctrl and click on all desired categories
                            </RBForm.Text>
                        </RBForm.Group>
                        


                        <RBForm.Group>
                            <RBForm.Label>Price</RBForm.Label>
                            <RBForm.Control
                                type="number"
                                step="0.01"
                                min="0"
                                name="price"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.price}
                            />
                            <RBForm.Text className="text-muted">
                                How much is going to be the product sold for?
                            </RBForm.Text>
                            {errors.price && touched.price && errors.price}
                        </RBForm.Group>



                        <RBForm.Group>
                            <RBForm.Label>Cost</RBForm.Label>
                            <RBForm.Control
                                type="number"
                                step="0.01"
                                min="0"
                                name="cost"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.cost}
                            />
                            <RBForm.Text className="text-muted">
                                How much does the product cost us?
                            </RBForm.Text>
                            {errors.cost && touched.cost && errors.cost}
                        </RBForm.Group>
                        
                        <RBForm.Group>
                            <RBForm.Label>Stock</RBForm.Label>
                            <RBForm.Control
                                type="number"
                                step="1"
                                min="0"
                                name="current_stock"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.current_stock}
                            />
                            {errors.current_stock && touched.current_stock && errors.current_stock}
                        </RBForm.Group>
                        
                        
                        <Button type="submit" disabled={isSubmitting}>
                            Submit
                        </Button>
                    </RBForm>
                    
                )}
            </Formik>
                </Card>
            </Col>
        </Row>
        

    </Container>
};

export default AddProductForm;