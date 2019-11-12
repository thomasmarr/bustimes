import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import Navbar from './components/Navbar'
import Form from './components/Form'
import DataRenderer from './components/DataRenderer'
import NotFound from './components/NotFound'

import { ThemeProvider } from 'styled-components'
import * as S from './Styles'
import { PurpleTheme, LightTheme } from './Themes'

const App = () => {
  const [theme, setTheme] = useState(PurpleTheme)

  const toggleTheme = () => {
    if (theme === PurpleTheme) {
      setTheme(LightTheme)
    } else {
      setTheme(PurpleTheme)
    }
  }

  const renderFromNaptan = (props) => {
    return <DataRenderer {...props} url={`http://localhost:8080/api/live-arrivals/naptan/${props.match.params.naptanid}`} title="Live Bus Arrival Times" />
  }
  const renderFromSms = (props) => {
    return <DataRenderer {...props} url={`http://localhost:8080/api/live-arrivals/${props.match.params.smscode}`} title="Live Bus Arrival Times" message="This page can be bookmarked or saved to your home screen for easy access."/>
  }
  const renderFromHistory = (props) => {
    return <DataRenderer {...props} url={`http://localhost:8080/api/get-history`} title="Bus Times Request History" />
  }
  return (
    <ThemeProvider theme={theme}>
      <S.Global />
      <Router>
        <Navbar />
        <S.ContentWrapper>
          <Switch>
            <Route path="/" exact component={Form} />
            <Route path="/history" render={renderFromHistory} />
            <Route path="/livearrivals/naptan/:naptanid" exact render={renderFromNaptan} />
            <Route path="/livearrivals/:smscode" render={renderFromSms} />
            <Route path="/livearrivals" component={Form} />
            <Route component={NotFound}/>
          </Switch>
        </S.ContentWrapper>
      </Router>
      <S.ThemeButton className="btn-floating btn-large waves-effect waves-light" onClick={toggleTheme}>
        {theme === PurpleTheme ? 
          (<i class="material-icons">wb_sunny</i>)
          :
          (<i class="material-icons">brightness_3</i>)}
      </S.ThemeButton>
    </ThemeProvider>
  );
}

export default App;
