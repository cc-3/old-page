import React from 'react';

import { signIn } from '../../firebase';


export default class Login extends React.Component {

  render() {
    return (
      <div className="cc-3-login">
        <div className="card-panel z-depth-2 cc-3-login-box">
          <div className="center">
            <img src="/img/logo.png" alt="Autograders" className="responsive-img" />
          </div>
          <button
            onClick={signIn}
            title="Sign In with Google"
            className="waves-effect waves-light btn cc-3-login-btn google">
            Sign In with Google
            <i className="fab fa-google left"></i>
          </button>
        </div>
      </div>
    );
  }

}
