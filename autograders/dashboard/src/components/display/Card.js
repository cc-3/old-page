import React from 'react';
import { Link } from 'react-router-dom';


const Card = ({ title, subtitle='', color='red', to, modal=false, trigger='' }) => (
  !modal ?
    <div className="card">
      <div className="card-image">
        <Link to={to}>
          <div className={`${color}`} style={{minHeight: 200}}></div>
          <span className="card-title">{title} {subtitle}</span>
        </Link>
      </div>
    </div>
  :
    <div className="card">
      <div className="card-image modal-trigger" href={`#${trigger}`} style={{cursor: 'pointer'}}>
        <div className={`${color}`} style={{minHeight: 200}}></div>
        <span className="card-title">{title} {subtitle}</span>
      </div>
    </div>
);


export default Card;
