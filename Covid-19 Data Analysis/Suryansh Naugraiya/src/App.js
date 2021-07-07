import React from 'react';
import './App.css';
import {Route, Link, Switch, NavLink} from 'react-router-dom';
import Home from './Home';
import CountryPage from './CountryPage';
import HistoryPage from './HistoryPage';
import AboutPage from './AboutPage';
import {Provider} from './Context';

function App() {
  return (
    <Provider>
      <div className="App">
        <Switch>
          <Route exact path='/' render={(routeProps) => <Home {...routeProps}/>} />
          <Route exact path='/country' render={() => <CountryPage />} />
          <Route exact path='/history' render={() => <HistoryPage />} />
          <Route exact path='/about' render={() => <AboutPage />} />
        </Switch>
      </div>
    </Provider>
  );
}

// function App(){
//   return(
//     <div>
//       <Provider></Provider>
//     </div>
//   )
// }

export default App;