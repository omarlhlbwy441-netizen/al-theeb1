
import React, { useState } from 'react';

function App() {
  const [balance, setBalance] = useState(500); // رصيد تجريبي

  const handleBuy = (productName) => {
    alert(`تم إرسال طلب شراء لـ: ${productName} - سيتم خصم الرصيد من المحفظة.`);
    setBalance(balance - 150);
  };

  return (
    <div style={{ padding: '20px', backgroundColor: '#121212', color: '#fff' }}>
      <h1>🛒 متجر منظومة التصنيع</h1>
      <h3>رصيد محفظتك: {balance} DC</h3>
      <div style={{ display: 'grid', gap: '15px' }}>
         <div style={{ padding: '15px', border: '1px solid #444' }}>
            <h4>تطبيق إدارة المهام الذكي</h4>
            <p>السعر: 150 DC</p>
            <button onClick={() => handleBuy("تطبيق إدارة المهام")}>شراء الآن</button>
         </div>
      </div>
    </div>
  );
}
export default App;
