import React from 'react';
import numeral from 'numeral';

import { attach, dettach } from '../../utils';


export default class Footer extends React.Component {

  state = {
    online: false,
    size: 0
  };

  handleStatus = (status) => {
    this.setState({online: status});
  };

  handleQueue = (size) => {
    this.setState({size})
  };

  componentWillMount() {
    attach('/server/status', this.handleStatus);
    attach('/queue_size', this.handleQueue);
  }

  componentWillUnmount() {
    dettach('/server/status', this.handleStatus);
    dettach('/queue_size', this.handleQueue);
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
            Server Status: {server} (queue size: {numeral(this.state.size).format('0,0')})
            <a href="https://www.github.com/cc-3" className="right cc-3-footer-link">
              <i className="fab fa-github cc-3-footer-icon" /> Github
            </a>
          </div>
        </div>
      </footer>
    );
  }

}
