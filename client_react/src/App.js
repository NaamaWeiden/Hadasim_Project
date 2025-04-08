// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ManagerPage from './pages/Manager/ManagerPage';
import SupplierPage from './pages/Suppliers/SupplierPage';
import RegisterSupplier from './pages/Suppliers/RegisterSupplier';
import SupplierLogin from './pages/Suppliers/SupplierLogin';
import OrderFormPage from './pages/Manager/OrderFormPage';
// import ViewOrdersPage from './pages/Manager/ViewOrdersPage';
// import ConfirmOrderPage from './pages/Manager/ConfirmOrderPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/manager" element={<ManagerPage />} />
        <Route path="/supplier" element={<SupplierPage />} />
        <Route path="/register-supplier" element={<RegisterSupplier />} />
        <Route path="/supplier-login" element={<SupplierLogin />} />
        <Route path="/order" element={<OrderFormPage />} />
        {/* <Route path="/view-orders" element={<ViewOrdersPage />} /> */}
        {/* <Route path="/confirm-order" element={<ConfirmOrderPage />} /> */}

      </Routes>
    </Router>
  );
}

export default App;
