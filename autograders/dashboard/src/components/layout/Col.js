import React from 'react';


const Col = ({ size='s12', children }) => (
  <div className={`col ${size}`}>
    {children}
  </div>
);


export default Col;
