import React from 'react';

import Row from './Row';
import Col from './Col';


const Content = ({ children }) => (
  <div className="sticky-content">
    <div className="cc-3-container">
      <Row>
        <Col>{children}</Col>
      </Row>
    </div>
  </div>
);


export default Content;
