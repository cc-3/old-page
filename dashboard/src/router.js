import React from 'react';
import createHistory from 'history/createBrowserHistory';
import { Router, Route, Switch, Redirect } from 'react-router-dom';

import Labs from './components/pages/Labs';
import Login from './components/pages/Login';
import Console from './components/pages/Console';
import Projects from './components/pages/Projects';
import Dashboard from './components/pages/Dashboard';

// browser history
const history = createHistory();

// default app router
const AppRouter = () => (
  <Router history={history}>
    <Switch>
      <Route path="/login" component={Login} exact />
      <Route path="/dashboard" component={Dashboard} exact />
      <Route path="/labs" component={Labs} exact />
      <Route path="/projects" component={Projects} exact />
      <Route path="/console/:id" component={Console} exact />
      <Route render={() => <Redirect to="/dashboard" />} />
    </Switch>
  </Router>
);


export { AppRouter, history};
