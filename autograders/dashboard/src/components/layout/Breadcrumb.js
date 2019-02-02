import React from 'react';
import { Link } from 'react-router-dom';


const Breadcrumb = ({ paths=[], names=[] }) => (
  (paths.length !== 0 && paths.length === names.length) ?
    <nav>
      <div className="nav-wrapper red">
        <div className="col s12">
          {
            paths.map((e, i) => <Link to={e} key={e} className="breadcrumb">{names[i]}</Link>)
          }
        </div>
      </div>
    </nav>
  :
    null
);


export default Breadcrumb;
