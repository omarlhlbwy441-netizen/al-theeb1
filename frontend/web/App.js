
import React, { useState } from 'react';

function App() {
  const [balance, setBalance] = useState(350.0);
  const [videoPrompt, setVideoPrompt] = useState("");
  const [logs, setLogs] = useState(["النظام جاهز للتشغيل."]);

  const handleVideoGen = () => {
    if (balance >= 50.0) {
      setBalance(balance - 50.0);
      setLogs([`تم إرسال طلب: "${videoPrompt}" - جاري التوليد...`, ...logs]);
      alert("تم بدء التوليد، سيتم خصم 50 DC من محفظتك.");
    } else {
      alert("رصيد غير كافٍ!");
    }
  };

  return (
    <div style={{ padding: '30px', backgroundColor: '#f4f4f9', fontFamily: 'Arial' }}>
      <h1>🏢 مركز قيادة منظومة design - الإصدار الشامل</h1>
      
      {/* قسم المحفظة */}
      <div style={{ background: '#fff', padding: '20px', borderRadius: '10px', marginBottom: '20px' }}>
        <h2>💰 المحفظة: {balance} DC</h2>
      </div>

      {/* استوديو الفيديو */}
      <div style={{ background: '#fff', padding: '20px', borderRadius: '10px', marginBottom: '20px' }}>
        <h2>🎥 استوديو الفيديو الذكي</h2>
        <input 
            type="text" 
            placeholder="اكتب وصف الفيديو هنا..." 
            value={videoPrompt}
            onChange={(e) => setVideoPrompt(e.target.value)}
            style={{ width: '70%', padding: '10px' }}
        />
        <button onClick={handleVideoGen} style={{ marginLeft: '10px', padding: '10px', background: '#d9534f', color: '#fff', border: 'none' }}>
            توليد الفيديو (50 DC)
        </button>
      </div>

      {/* سجل الأحداث */}
      <div style={{ background: '#333', color: '#fff', padding: '20px', borderRadius: '10px' }}>
        <h3>📜 سجل العمليات</h3>
        {logs.map((log, i) => <p key={i}>{log}</p>)}
      </div>
    </div>
  );
}
export default App;
