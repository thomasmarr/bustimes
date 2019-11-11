import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom'

import Navbar from './components/Navbar'
import LiveArrivals from './components/LiveArrivals'
import History from './components/History'

import { ThemeProvider } from 'styled-components'
import * as S from './Styles'
import { PurpleTheme } from './Themes'

const App = () => {
  const data = fetch('http://localhost:8080/api/data')
    .then(response => response.json())
    .then(json => console.log('👌', json))
  return (
    <ThemeProvider theme={PurpleTheme}>
      <S.Global />
      <Router>
        <Navbar />
        <S.ContentWrapper>
          <div>
            React App
        </div>
          <Route path="/" exact component={LiveArrivals} />
          <Route path="/history" component={History} />
        </S.ContentWrapper>
      </Router>
    </ThemeProvider>
  );
}

export default App;
