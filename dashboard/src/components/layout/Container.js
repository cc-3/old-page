import React from 'react';

import NavBar from './NavBar';
import Footer from './Footer';


const Container = ({ children }) => (
  <div className="sticky-wrap">
    <NavBar/>
      {children}
    <Footer/>
  </div>
);


export default Container;
