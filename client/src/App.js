import React from 'react';

const App = () => {
  const data = fetch('http://localhost:8080/api/data')
    .then(response=>response.json())
    .then(json=>console.log('👌',json))
  return (
    <div>
      React App
    </div>
  );
}

export default App;
