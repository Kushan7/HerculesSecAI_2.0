import React, { useState } from 'react';
import ApiStatus from '../components/ApiStatus';

export default function Home() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);

    const res = await fetch('http://localhost:8000/scan', {
      method: 'POST',
      body: formData,
    });

    const data = await res.json();
    setResult(JSON.stringify(data, null, 2));
  };

  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-bold">🔐 Hercules Secure</h1>
      <ApiStatus />
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button type="submit" className="ml-2 p-1 bg-blue-600 rounded">Scan</button>
      </form>
      {result && <pre className="bg-gray-800 p-4 rounded">{result}</pre>}
    </div>
  );
}