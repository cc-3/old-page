import React from 'react';

import Col from '../layout/Col';

import { getRandomEmoji } from '../../utils';


const Emoji = ({ text='Machine Structures' }) => (
  <Col size="s12">
    <h1 className="center grey-text notfound">{getRandomEmoji()}</h1>
    <h6 className="center grey-text text-lighten-1">{text}</h6>
  </Col>
);


export default Emoji;
