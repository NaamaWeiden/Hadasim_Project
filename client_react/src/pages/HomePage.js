// src/pages/HomePage.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './homePage.css';

function HomePage() {
  const [showPassword, setShowPassword] = useState(false);
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleManagerClick = () => {
    setShowPassword(true);
  };

  const handlePasswordSubmit = () => {
    if (password === '1234') {
      navigate('/manager');
    } else {
      alert('סיסמה שגויה');
    }
  };

  return (
    <div className="home-container">
      <h1 className="home-title">ברוכים הבאים</h1>

      <button className="home-button" onClick={() => navigate('/supplier')}>
        כניסת ספקים
      </button>

      <button className="home-button" onClick={handleManagerClick}>
        כניסת בעל החנות
      </button>

      {showPassword && (
        <div className="password-container">
          <input
            type="password"
            placeholder="הכנס סיסמה"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="password-input"
          />
          <button className="home-button" onClick={handlePasswordSubmit}>
            אישור
          </button>
        </div>
      )}
    </div>
  );
}

export default HomePage;
