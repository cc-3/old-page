import React from 'react';
import { NavLink } from 'react-router-dom';

import { auth, signOut } from '../../firebase';


const NavBarLink = ({ to, text, icon, raw=false }) => {
  if (!raw)
    return (
      <li className="cc-3-nav-hov">
        <NavLink
          to={to}
          activeClassName="cc-3-active-link"
          className="cc-3-link waves-effect white-text">
          <i className={`fas fa-${icon} grey-text left`}></i>
          {text}
        </NavLink>
      </li>
    );
  return (
    <li>
      <a href={to} target="_blank" rel="noopener noreferrer" className="cc-3-link waves-effect white-text">
        <i className={`fas fa-${icon} grey-text left`}></i>
        {text}
      </a>
    </li>
  );
}


export default class Navbar extends React.Component {

  componentDidMount() {
    const elem = document.getElementById('slide-out');
    window.M.Sidenav.init(elem);
    const modal = document.getElementById('token');
    window.M.Modal.init(modal);
  }

  render() {
    return (
      <div>
        <nav className="cc-3-navbar grey darken-4">
          <div className="nav-wrapper">
            {/* eslint-disable-next-line */}
            <a data-target="slide-out" className="sidenav-trigger">
              <i className="material-icons">menu</i>
            </a>
            <ul id="mobile" className="right hide-on-med-and-down">
              <li>
                {/* eslint-disable-next-line */}
                <a title="Log Out" onClick={signOut} className="cc-3-logout">
                  <i className="material-icons">exit_to_app</i>
                </a>
              </li>
            </ul>
          </div>
        </nav>
        <div id="token" className="modal">
          <div className="modal-content">
            <h4 className="center">{auth.currentUser.uid}</h4>
          </div>
        </div>
        <ul id="slide-out" className="sidenav sidenav-fixed grey darken-4">
          <div className="user-view pl-user-view">
            <div className="background">
              <img src="/img/bg.jpg" alt="sidenav background" width="100%"/>
            </div>
            <img className="circle" src={auth.currentUser.photoURL} alt="Profile"/>
            <span className="white-text name">
              {auth.currentUser.displayName}
            </span>
            <span className="white-text email">
              {auth.currentUser.email}
            </span>
          </div>
          {/* eslint-disable-next-line */}
          <li><a className="subheader grey-text">Autograders</a></li>
          <NavBarLink to="/dashboard" text="Dashboard" icon="home" />
          <NavBarLink to="/labs" text="Labs" icon="flask" />
          <NavBarLink to="/projects" text="Projects" icon="project-diagram" />
          {/* eslint-disable-next-line */}
          <li><a className="subheader grey-text">Resources</a></li>
          <NavBarLink raw to="https://cc-3.github.io/" text="Web Page" icon="school" />
          <NavBarLink raw to="http://riscbook.com/" text="RISC-V Book" icon="book" />
        </ul>
      </div>
    );
  }
}
