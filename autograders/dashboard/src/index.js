import React from 'react';
import ReactDOM from 'react-dom';

import "react-vis/dist/style.css";

import './style.css';
import { auth } from './firebase';
import { history, AppRouter } from './router';


let hasRendered = false;
const renderApp = () => {
  if (!hasRendered) {
    hasRendered = true;
    ReactDOM.render(<AppRouter />, document.getElementById('root'));
  }
};

// auth state handler
auth.onAuthStateChanged((user) => {
  if (user) {
    if (history.location.pathname === '/login')
      history.push('/dashboard');
    renderApp();
  } else {
    history.push('/login');
    renderApp();
  }
});
