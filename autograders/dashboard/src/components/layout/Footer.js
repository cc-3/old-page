import React from 'react';

import { attach, dettach } from '../../utils';


export default class Footer extends React.Component {

  state = {
    online: false
  };

  handleStatus = (status) => {
    this.setState({online: status});
  };

  componentWillMount() {
    attach('/server/status', this.handleStatus);
  }

  componentWillUnmount() {
    dettach('/server/status', this.handleStatus);
  }

  render() {
    const { online } = this.state;
    const on = <i className="fas fa-dot-circle green-text" />;
    const off = <i className="fas fa-circle red-text"/>
    const server = online ? on : off;
    return (
      <footer className="page-footer cc-3-footer">
        <div className="footer-copyright cc-3-copyright">
          <div className="container">
            Server Status: {server}
            <a href="https://www.github.com/cc-3" className="right cc-3-footer-link">
              <i className="fab fa-github cc-3-footer-icon" /> Github
            </a>
          </div>
        </div>
      </footer>
    );
  }

}
