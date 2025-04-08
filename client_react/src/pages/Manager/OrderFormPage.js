// src/pages/Manager/OrderFormPage.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './managerPages.css';

const OrderFormPage = () => {
  const [suppliers, setSuppliers] = useState([]);
  const [products, setProducts] = useState([]);
  const [formData, setFormData] = useState({
    invitation_id: '',
    company_name: '',
    product_name: '',
    quantity: '',
    minimum_for_sale: '',
    total_payment: ''
  });

  useEffect(() => {
    axios.get('http://localhost:5000/get_suppliers')
    .then(res => setSuppliers(res.data))
      .catch(err => console.error('שגיאה בשליפת שמות ספקים', err));
  }, []);

  const handleCompanyChange = (e) => {
    const selectedCompany = e.target.value;
    setFormData({ ...formData, company_name: selectedCompany, product_name: '', quantity: '', minimum_for_sale: '', total_payment: '' });

    axios.get(`http://localhost:5000/get_products_by_supplier?company_name=${encodeURIComponent(selectedCompany)}`)
  .then(res => setProducts(res.data))
  .catch(err => console.error('שגיאה בשליפת מוצרים', err));

  };

  const handleProductChange = (e) => {
    const selectedProduct = e.target.value;
    setFormData(prev => ({ ...prev, product_name: selectedProduct, quantity: '', total_payment: '' }));

    axios.get(`http://localhost:5000/get_minimum_for_sale?product_name=${encodeURIComponent(selectedProduct)}`)
    .then(res => setFormData(prev => ({ ...prev, minimum_for_sale: res.data })))
      .catch(err => console.error('שגיאה בשליפת מינימום למכירה', err));
  };

  const handleQuantityChange = (e) => {
    const quantity = parseInt(e.target.value);
    setFormData(prev => ({ ...prev, quantity }));

    if (!isNaN(quantity) && formData.product_name) {
        axios.get(`http://localhost:5000/calculate_total_payment?product_name=${encodeURIComponent(formData.product_name)}&quantity=${quantity}`)
        .then(res => setFormData(prev => ({ ...prev, total_payment: res.data })))
        .catch(err => console.error('שגיאה בחישוב תשלום כולל', err));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post('http://localhost:5000/add_invitation', formData);
      alert('ההזמנה נוספה בהצלחה');
      setFormData({ invitation_id: '', company_name: '', product_name: '', quantity: '', minimum_for_sale: '', total_payment: '' });
    } catch (err) {
      alert('שגיאה בהוספת ההזמנה: ' + err.response?.data?.error);
    }
  };

  return (
    <div className="manager-container">
      <h2 className="manager-title">טופס הזמנת סחורה</h2>
      <form onSubmit={handleSubmit} className="order-form">
        <input
          type="text"
          placeholder="מספר הזמנה"
          value={formData.invitation_id}
          onChange={(e) => setFormData({ ...formData, invitation_id: e.target.value })}
          required
        />

        <select value={formData.company_name} onChange={handleCompanyChange} required>
          <option value="">בחר ספק</option>
          {suppliers.map((name, i) => <option key={i} value={name}>{name}</option>)}
        </select>

        <select value={formData.product_name} onChange={handleProductChange} required>
          <option value="">בחר מוצר</option>
          {products.map((product, i) => <option key={i} value={product}>{product}</option>)}
        </select>

        {formData.minimum_for_sale && (
          <div>מינימום להזמנה: {formData.minimum_for_sale}</div>
        )}

        <input
          type="number"
          placeholder="כמות"
          value={formData.quantity}
          onChange={handleQuantityChange}
          required
        />

        {formData.total_payment && (
          <div>סה"כ לתשלום: {formData.total_payment} ש"ח</div>
        )}

        <button type="submit" className="manager-button">שלח הזמנה</button>
      </form>
    </div>
  );
};

export default OrderFormPage;
