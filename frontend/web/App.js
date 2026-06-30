
import React, { useState } from 'react';

function App() {
  const [stats, setStats] = useState({ total_products: 1, total_value: 150.0 });

  return (
    <div style={{ padding: '30px', backgroundColor: '#f4f4f9', fontFamily: 'Arial' }}>
      <h1>🏢 مركز قيادة منظومة design</h1>
      
      <div style={{ display: 'flex', gap: '20px', marginBottom: '30px' }}>
        <div style={{ padding: '20px', background: '#fff', borderRadius: '10px', flex: 1 }}>
          <h3>القيمة السوقية الكلية</h3>
          <p style={{ fontSize: '2em', color: '#007bff' }}>{stats.total_value} DC</p>
        </div>
        <div style={{ padding: '20px', background: '#fff', borderRadius: '10px', flex: 1 }}>
          <h3>إجمالي الأنظمة المبتكرة</h3>
          <p style={{ fontSize: '2em', color: '#28a745' }}>{stats.total_products}</p>
        </div>
      </div>
      {/* باقي مكونات الواجهة (المتجر، المحفظة) ... */}
    </div>
  );
}
export default App;
