
import React, { useState, useEffect } from 'react';

function App() {
  const [balance, setBalance] = useState(350.0);
  const [products, setProducts] = useState([
    { id: 'PRJ-1782847084', name: 'تطبيق إدارة المهام الذكي', price: 150.0 }
  ]);
  const [history, setHistory] = useState([]);

  const handlePurchase = (product) => {
    if (balance >= product.price) {
      setBalance(balance - product.price);
      setHistory([...history, `تم شراء ${product.name} بنجاح!`]);
      alert(`مبروك! تم شراء ${product.name}`);
    } else {
      alert("رصيد غير كافٍ!");
    }
  };

  return (
    <div style={{ padding: '30px', fontFamily: 'Arial', backgroundColor: '#f4f4f9', minHeight: '100vh' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', padding: '20px', background: '#333', color: '#fff', borderRadius: '10px' }}>
        <h1>🏢 منظومة design - لوحة التحكم التنفيذية</h1>
        <div style={{ fontSize: '1.2em', fontWeight: 'bold' }}>رصيد المحفظة: {balance} DC</div>
      </header>

      <section style={{ marginTop: '30px' }}>
        <h2>🛒 متجر الأنظمة الجاهزة</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px' }}>
          {products.map(p => (
            <div key={p.id} style={{ background: '#fff', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 5px rgba(0,0,0,0.1)' }}>
              <h3>{p.name}</h3>
              <p>السعر: {p.price} DC</p>
              <button onClick={() => handlePurchase(p)} style={{ background: '#28a745', color: '#fff', border: 'none', padding: '10px', borderRadius: '5px', cursor: 'pointer' }}>شراء الآن</button>
            </div>
          ))}
        </div>
      </section>

      <section style={{ marginTop: '30px' }}>
        <h2>📜 سجل العمليات (Audit Log)</h2>
        <ul style={{ background: '#fff', padding: '20px', borderRadius: '8px' }}>
          {history.length === 0 ? <p>لا توجد عمليات بعد.</p> : history.map((log, i) => <li key={i}>{log}</li>)}
        </ul>
      </section>
    </div>
  );
}

export default App;
