import React, { useState, useEffect } from "react";
import { Formik } from "formik";
import { Form as RBForm, Container, Row, Col, Card } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import axios from "axios";
import * as Yup from "yup";
import { useNavigate, useParams } from "react-router-dom";

const ProductForm = () => {
    const navigate = useNavigate();
    const { id } = useParams(); // To get the product ID from the URL for editing
    const [categories, setCategories] = useState([]);
    const [initialValues, setInitialValues] = useState({
        name: "",
        description: "",
        price: "",
        cost: "",
        current_stock: "",
        category_ids: [],
    });

    useEffect(() => {
        axios
        .get("http://localhost:5000/categories")
        .then((response) => {
            setCategories(response.data.categories);
        })
        .catch((err) => {
            console.error("Error fetching categories: " + err);
        });

        if (id) {
        axios
            .get(`http://localhost:5000/products/${id}`)
            .then((response) => {
            const product = response.data.product;
            setInitialValues({
                name: product.name,
                description: product.description,
                price: product.price,
                cost: product.cost,
                current_stock: product.current_stock,
                category_ids: product.category_ids,
            });
            })
            .catch((err) => {
            console.error("Error fetching product: " + err);
            });
        }
    }, [id]);

    const saveProduct = (product, setSubmitting) => {
        const request = id
        ? axios.put(`http://localhost:5000/products/${id}`, product, {
            headers: {
                "Content-Type": "application/json",
            },
            })
            .then(response => {
                console.log("Product updated successfully: ", response.data);
                navigate("/products/" + id);
            })
            .catch(err => {
                console.error("There was an error with updating this product: ", err);
            })
        : axios.post("http://localhost:5000/products", product, {
            headers: {
                "Content-Type": "application/json",
            },
            })
            .then(response => {
                console.log("Product created successfully: ", response.data);
                navigate("/products/" + response.data.product.id)
            })

        request
        .finally(() => {
            setSubmitting(false);
        });
    };

    const formField = (
        label,
        value,
        text,
        type,
        fieldName,
        errors,
        touched,
        handleChange,
        handleBlur,
        step,
        setFieldValue
    ) => {
        const inputProps = {};
        if (type === "number") {
        inputProps.step = step || 1;
        inputProps.min = 0;
        }

        if (type === "selection") {
        return (
            <RBForm.Group key={fieldName}>
            <RBForm.Label>{label}</RBForm.Label>
            <RBForm.Control
                as="select"
                name={fieldName}
                multiple
                onChange={(e) => {
                const selectedOptions = Array.from(e.target.selectedOptions).map(
                    (option) => option.value
                );
                setFieldValue(fieldName, selectedOptions);
                }}
                onBlur={handleBlur}
                value={value}
            >
                {categories.length > 0 ? (
                categories.map((item) => (
                    <option key={item.id} value={item.id}>
                    {item.name}
                    </option>
                ))
                ) : (
                <option disabled>No {label} available</option>
                )}
            </RBForm.Control>
            <RBForm.Text className="text-muted">{text}</RBForm.Text>
            </RBForm.Group>
        );
        } else {
        return (
            <RBForm.Group className="mb-3" key={fieldName}>
            <RBForm.Label>{label}</RBForm.Label>
            <RBForm.Control
                type={type}
                name={fieldName}
                onChange={handleChange}
                onBlur={handleBlur}
                value={value}
                {...inputProps}
            />
            <RBForm.Text>{text}</RBForm.Text>
            {errors[fieldName] && touched[fieldName] && errors[fieldName]}
            </RBForm.Group>
        );
        }
    };

    const productObjectMapper = (product) => {
        return {
        name: product.name,
        description: product.description,
        price: product.price,
        cost: product.cost,
        discontinued: false,
        current_stock: product.current_stock,
        category_ids: product.category_ids.join(","),
        };
    };

    return (
        <Container className="justify-content-center align-items-center vh-100">
        <Row className="w-100">
            <Col md={{ span: 8, offset: 2 }}>
            <Card className="p-4" style={{ backgroundColor: "#f5f5f5" }}>
                <Formik
                initialValues={initialValues}
                enableReinitialize
                validationSchema={Yup.object({
                    name: Yup.string().required("Required"),
                    description: Yup.string(),
                    price: Yup.number().min(0).required("Required"),
                    cost: Yup.number().min(0).required("Required"),
                    current_stock: Yup.number().min(0).required("Required"),
                    category_ids: Yup.array().of(Yup.string()),
                })}
                onSubmit={(values, { setSubmitting, resetForm }) => {
                    const product = productObjectMapper(values);
                    saveProduct(product, setSubmitting);
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
                    setFieldValue,
                }) => (
                    <RBForm onSubmit={handleSubmit}>
                    {formField(
                        "Name",
                        values.name,
                        "Product's name",
                        "text",
                        "name",
                        errors,
                        touched,
                        handleChange,
                        handleBlur
                    )}

                    {formField(
                        "Description",
                        values.description,
                        "Product's description",
                        "text",
                        "description",
                        errors,
                        touched,
                        handleChange,
                        handleBlur
                    )}

                    {formField(
                        "Categories",
                        values.category_ids,
                        "Hold Ctrl and click on all desired categories",
                        "selection",
                        "category_ids",
                        errors,
                        touched,
                        handleChange,
                        handleBlur,
                        null,
                        setFieldValue
                    )}

                    {formField(
                        "Price",
                        values.price,
                        "How much is the product going to be sold for?",
                        "number",
                        "price",
                        errors,
                        touched,
                        handleChange,
                        handleBlur,
                        "0.01"
                    )}

                    {formField(
                        "Cost",
                        values.cost,
                        "How much does the product cost us?",
                        "number",
                        "cost",
                        errors,
                        touched,
                        handleChange,
                        handleBlur,
                        "0.01"
                    )}

                    {formField(
                        "Stock",
                        values.current_stock,
                        "How many do we have?",
                        "number",
                        "current_stock",
                        errors,
                        touched,
                        handleChange,
                        handleBlur
                    )}

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
    );
};

export default ProductForm;
