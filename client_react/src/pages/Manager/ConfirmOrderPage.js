import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './managerPages.css';

const ConfirmOrderPage = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      const response = await axios.get('http://localhost:5000/get_in_process_invitations');
      setOrders(response.data);
    } catch (error) {
      console.error('שגיאה בשליפת הזמנות:', error);
    }
  };

  const handleConfirm = async (invitationId) => {
    try {
      await axios.put(`http://localhost:5000/complete_invitation/${invitationId}`);
      fetchOrders(); // רענון הנתונים אחרי אישור
    } catch (error) {
      console.error('שגיאה באישור ההזמנה:', error);
    }
  };

  return (
    <div className="manager-container">
      <h2 className="manager-title">אישור הזמנות בתהליך</h2>
      {orders.length === 0 ? (
        <p>אין הזמנות לאישור</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>מזהה</th>
              <th>מוצר</th>
              <th>חברה</th>
              <th>כמות</th>
              <th>תשלום כולל</th>
              <th>סטטוס</th>
              <th>פעולה</th>
            </tr>
          </thead>
          <tbody>
            {orders.map((order) => (
              <tr key={order.invitation_id}>
                <td>{order.invitation_id}</td>
                <td>{order.product_name}</td>
                <td>{order.company_name}</td>
                <td>{order.quantity}</td>
                <td>{order.total_payment}</td>
                <td>{order.status}</td>
                <td>
                  {order.status === 'בתהליך' && (
                    <button className="confirm-button" onClick={() => handleConfirm(order.invitation_id)}>
                    אשר הזמנה
                  </button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default ConfirmOrderPage;
