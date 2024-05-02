import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

import Home from './pages/Home';
import Header from './components/Header';
import ProductPage from './pages/ProductPage';

const App = () => {
  return <Router>
    <Header />
    <Routes>
      <Route path='/' element ={<Home />} />
      <Route path='/products' element={<ProductPage />} />
    </Routes>
  </Router>
}

export default App;