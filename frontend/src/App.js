import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Home from './pages/Home';
import Header from './components/Header';
import ProductPage from './pages/ProductPage';
import ProductDetailsPage from './pages/ProductDetailsPage';
import AddProductPage from './pages/AddProductPage';

const App = () => {
  return <Router>
    <Header />
    <Routes>
      <Route path='/' element ={<Home />} />
      <Route path='/products' element={<ProductPage />} />
      <Route path='/products/:id' element={<ProductDetailsPage />} />
      <Route path='/products/new' element={<AddProductPage />} />
    </Routes>
  </Router>
}

export default App;