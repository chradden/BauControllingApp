
import React, { useEffect, useState } from 'react'

function App() {
  const [health, setHealth] = useState<string>('checking...')

  useEffect(() => {
    // Nutze den konfigurierten Proxy
    fetch('/api/health').then(r => r.json()).then(d => {
      setHealth(d.status || 'unknown')
    }).catch(() => setHealth('offline'))
  }, [])

  return (
    <div style={{ padding: 24, fontFamily: 'sans-serif' }}>
      <h1>🧱 Bau-Controlling App</h1>
      <p>Backend health: <strong>{health}</strong></p>
      <ul>
        <li>DIN 276 Budget, Rechnungen, Prüfworkflow</li>
        <li>Schlussverwendungsnachweis (Export)</li>
      </ul>
    </div>
  )
}

export default App
