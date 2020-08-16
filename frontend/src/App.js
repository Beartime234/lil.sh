import React from 'react';

import Routes from './routes';
import AppLayout from './layouts/AppLayout';
import ThemeProvider from './contexts/ThemeContext';
import './styles/index.scss';

import { createBrowserHistory } from 'history';


const history = createBrowserHistory();

const path = (/#!(\/.*)$/.exec(location.hash) || [])[1];
if (path) {
  history.replace(path);
}

function App() {

  return (
    <ThemeProvider>
      <AppLayout>
        <Routes />
      </AppLayout>
    </ThemeProvider>
  );
}

export default App;
