import React from 'react';
import { Link } from 'react-router-dom';


const getHeight = (width) => {
  const height = Math.floor(width / 1.8);
  if (Number.isNaN(height))
    return 300;
  return height;
};


const Card = ({ title, subtitle='', color='red', to, modal=false, trigger='', width }) => (
  !modal ?
    <div className="card">
      <div className="card-image">
        <Link to={to}>
          <div className={`${color}`} style={{minHeight: getHeight(width)}}></div>
          <span className="card-title title">{title} {subtitle}</span>
        </Link>
      </div>
    </div>
  :
    <div className="card">
      <div className="card-image modal-trigger" href={`#${trigger}`} style={{cursor: 'pointer'}}>
        <div className={`${color}`} style={{minHeight: getHeight(width)}}></div>
        <span className="card-title title">{title} {subtitle}</span>
      </div>
    </div>
);


export default Card;
