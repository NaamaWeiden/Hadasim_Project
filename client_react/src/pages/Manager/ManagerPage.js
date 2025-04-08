import React from 'react';
import { useNavigate } from 'react-router-dom';
import './managerPages.css';

const ManagerPage = () => {
  const navigate = useNavigate();

  return (
    <div className="manager-container">
      <h1 className="manager-title">ברוך הבא, מנהל</h1>
      <div className="manager-buttons">
        <button className="manager-button" onClick={() => navigate('/order')}>הזמנת סחורה</button>
        <button className="manager-button" onClick={() => navigate('/view-orders')}>צפייה בכל ההזמנות</button>
        <button className="manager-button" onClick={() => navigate('/confirm-order')}>אישור קבלת הזמנה</button>
      </div>
    </div>
  );
};

export default ManagerPage;
