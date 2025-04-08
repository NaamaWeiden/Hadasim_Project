import React, { useState } from 'react';
import './SupplierLogin.css';

const SupplierLogin = () => {
    const [companyName, setCompanyName] = useState('');
    const [completedInvitations, setCompletedInvitations] = useState([]);
    const [inProcessInvitations, setInProcessInvitations] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();

        // שליחה לשרת כדי להביא את ההזמנות של הספק
        const response = await fetch(`http://localhost:5000/get_supplier_invitations?company_name=${encodeURIComponent(companyName)}`);
        const data = await response.json();

        if (data.invitations) {
            const completed = data.invitations.filter(invitation => invitation.status === 'הושלמה');
            const inProcess = data.invitations.filter(invitation => invitation.status === '');

            setCompletedInvitations(completed);
            setInProcessInvitations(inProcess);
        } else {
            console.error('Failed to fetch invitations');
        }
    };

    const handleUpdateStatus = async (invitationId) => {
        // עדכון סטטוס הזמנה ל-"בתהליך"
        const response = await fetch('http://localhost:5000/update_invitation_status', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ invitation_id: invitationId, status: 'בתהליך' })
        });
        const data = await response.json();

        if (data.message === 'Status updated successfully') {
            setInProcessInvitations(inProcessInvitations.filter(inv => inv.invitation_id !== invitationId));
        } else {
            console.error('Failed to update status');
        }
    };

    return (
        <div className="supplier-login">
            <h2>כניסת ספק</h2>
            <form onSubmit={handleSubmit}>
                <label>שם החברה:</label>
                <input
                    type="text"
                    value={companyName}
                    onChange={(e) => setCompanyName(e.target.value)}
                    required
                />
                <button type="submit">היכנס</button>
            </form>

            <div className="orders">
                <h3>הזמנות הושלמו:</h3>
                <ul>
                    {completedInvitations.map(invitation => (
                        <li key={invitation.invitation_id}>
                            {invitation.product_name} - סטטוס: {invitation.status}
                        </li>
                    ))}
                </ul>

                <h3>הזמנות בתהליך:</h3>
                <ul>
                    {inProcessInvitations.map(invitation => (
                        <li key={invitation.invitation_id}>
                            {invitation.product_name} - סטטוס: {invitation.status}
                            <button onClick={() => handleUpdateStatus(invitation.invitation_id)}>אשר</button>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default SupplierLogin;
