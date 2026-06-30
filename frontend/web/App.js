
import React, { useState, useEffect } from 'react';

function App() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // الاتصال بمحرك المنظومة لجلب الأرشيف
    fetch('http://localhost:8000/api/projects')
      .then(response => response.json())
      .then(data => {
        if (data.status === 'success') {
          setProjects(data.projects);
        }
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching projects:', error);
        setLoading(false);
      });
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'system-ui', backgroundColor: '#1e1e1e', color: '#fff', minHeight: '100vh' }}>
      <h1>🚀 لوحة تحكم مصنع الأنظمة</h1>
      
      {loading ? (
        <p>جاري جلب بيانات الأرشيف من المحرك...</p>
      ) : (
        <div style={{ display: 'grid', gap: '20px', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))' }}>
          {projects.map((proj, index) => (
            <div key={index} style={{ border: '1px solid #444', padding: '15px', borderRadius: '8px', backgroundColor: '#2d2d2d' }}>
              <h2 style={{ color: '#4CAF50', margin: '0 0 10px 0' }}>📦 {proj.name}</h2>
              <p>عدد الملفات المنجزة: {proj.files_count}</p>
              <ul style={{ color: '#aaa' }}>
                {proj.files.map((file, fIndex) => (
                  <li key={fIndex}>{file}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
