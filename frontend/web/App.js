import React, { useState } from 'react';

export default function App() {
  const [balance, setBalance] = useState(500); // رصيد افتراضي للتجربة

  const handlePurchase = () => {
    if (balance >= 150) {
      setBalance(balance - 150);
      alert('تم شراء إضافة "محرك الألعاب" بنجاح وتم تفعيلها!');
    } else {
      alert('الرصيد غير كافٍ!');
    }
  };

  return (
    <div style={{ padding: '30px', fontFamily: 'Arial', direction: 'rtl' }}>
      <h1>👑 الذئب الأبيض الملكي - لوحة التحكم</h1>
      
      <div style={{ padding: '20px', backgroundColor: '#f0f0f0', borderRadius: '10px' }}>
        <h2>المحفظة المالية</h2>
        <p style={{ fontSize: '24px', fontWeight: 'bold' }}>الرصيد: {balance} عملة</p>
      </div>

      <div style={{ marginTop: '20px', padding: '20px', border: '2px solid #333', borderRadius: '10px' }}>
        <h2>🛒 متجر الإضافات</h2>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h3>محرك ألعاب Unity المتقدم</h3>
          <p>السعر: 150 عملة</p>
          <button 
            onClick={handlePurchase}
            style={{ padding: '10px 20px', backgroundColor: '#000', color: '#fff', cursor: 'pointer' }}>
            شراء الإضافة
          </button>
        </div>
      </div>
    </div>
  );
}
