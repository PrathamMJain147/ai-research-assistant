import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import Plot from 'react-plotly.js';

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const runResearch = async () => {
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:8000/research');
      setData(res.data);
    } catch (e) {
      alert("Error: Make sure backend is running on port 8000");
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '40px' }}>
      <h1>🔬 Autonomous Research Assistant</h1>
      <button onClick={runResearch} disabled={loading} style={{ padding: '10px 20px', fontSize: '16px' }}>
        {loading ? "Agents are Collaborating (Cycles 1-5)..." : "Start Autonomous Research"}
      </button>

      {data && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '40px', marginTop: '40px' }}>
          <div>
            <ReactMarkdown>{data.final_paper}</ReactMarkdown>
          </div>
          <div>
            <h3>Uncertainty Score: {data.confidence_scores.current_cycle}%</h3>
            <Plot 
              data={JSON.parse(data.plotly_json).data} 
              layout={JSON.parse(data.plotly_json).layout} 
              style={{ width: '100%', height: '400px' }}
            />
          </div>
        </div>
      )}
    </div>
  );
}
export default App;