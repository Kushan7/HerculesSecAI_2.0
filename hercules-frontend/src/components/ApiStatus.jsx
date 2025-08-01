import React, { useEffect, useState } from 'react';
import { api } from '../lib/api';

export default function ApiStatus() {
  const [status, setStatus] = useState('Checking...');

  useEffect(() => {
    api.get('/health')
      .then(res => setStatus(res.data?.status || 'Online'))
      .catch(() => setStatus('Offline'));
  }, []);

  return <div>API Status: <span>{status}</span></div>;
}