import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import Navbar from './components/Navbar'
import LiveArrivals from './components/LiveArrivals'
import Form from './components/Form'
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
          <Switch>
            <Route path="/" exact component={Form} />
            <Route path="/history" component={History} />
            <Route path="/livearrivals/:smscode" component={LiveArrivals} />
            <Route path="/livearrivals" component={Form} />
          </Switch>
        </S.ContentWrapper>
      </Router>
    </ThemeProvider>
  );
}

export default App;
