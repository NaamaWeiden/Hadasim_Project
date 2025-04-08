// src/pages/SuppliersPage.js
import React from 'react';
import { useNavigate } from 'react-router-dom';
import './SuppliersPage.css';

const SuppliersPage = () => {
  const navigate = useNavigate();

  return (
    <div className="suppliers-container">
      <h1>כניסת ספקים</h1>
      <button onClick={() => navigate('/register-supplier')}>רישום ספק חדש</button>
      <button onClick={() => navigate('/supplier-login')}>כניסת ספק</button>
    </div>
  );
};

export default SuppliersPage;
