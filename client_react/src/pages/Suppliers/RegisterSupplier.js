import React, { useState } from 'react';
import axios from 'axios';

const RegisterSupplier = () => {
  const [companyName, setCompanyName] = useState('');
  const [phoneNum, setPhoneNum] = useState('');
  const [workerName, setWorkerName] = useState('');
  const [products, setProducts] = useState([{ productName: '', pricePerItem: '', minimumForSale: '' }]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const supplierData = {
      company_name: companyName,
      phone_num: phoneNum,
      worker_name: workerName,
      products: products.map(product => ({
        product_name: product.productName,  // שינוי כאן
        price_per_item: product.pricePerItem,
        minimum_for_sale: product.minimumForSale
      }))
    };

    try {
      const response = await axios.post('http://localhost:5000/add_supplier', supplierData);
      console.log(response.data);
      alert('Supplier added successfully!');
    } catch (error) {
      console.error(error);
      alert('Error adding supplier.');
    }
  };

  const handleProductChange = (index, event) => {
    const values = [...products];
    values[index][event.target.name] = event.target.value;
    setProducts(values);
  };

  const handleAddProduct = () => {
    setProducts([...products, { productName: '', pricePerItem: '', minimumForSale: '' }]);
  };

  return (
    <div>
      <h1>Register New Supplier</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Company Name:
          <input type="text" value={companyName} onChange={(e) => setCompanyName(e.target.value)} />
        </label>
        <label>
          Phone Number:
          <input type="text" value={phoneNum} onChange={(e) => setPhoneNum(e.target.value)} />
        </label>
        <label>
          Worker Name:
          <input type="text" value={workerName} onChange={(e) => setWorkerName(e.target.value)} />
        </label>
        <div>
          <h2>Products</h2>
          {products.map((product, index) => (
            <div key={index}>
              <label>
                Product Name:
                <input type="text" name="productName" value={product.productName} onChange={(e) => handleProductChange(index, e)} />
              </label>
              <label>
                Price Per Item:
                <input type="text" name="pricePerItem" value={product.pricePerItem} onChange={(e) => handleProductChange(index, e)} />
              </label>
              <label>
                Minimum For Sale:
                <input type="text" name="minimumForSale" value={product.minimumForSale} onChange={(e) => handleProductChange(index, e)} />
              </label>
            </div>
          ))}
          <button type="button" onClick={handleAddProduct}>Add Product</button>
        </div>
        <button type="submit">Register Supplier</button>
      </form>
    </div>
  );
};

export default RegisterSupplier;
