import React from 'react';


const Loading = ({ loading }) => {
  if (loading) {
    return (
      <div title="Grading..." className="right preloader-wrapper active" style={{width: 14, height: 14}}>
        <div className="spinner-layer spinner-green-only">
          <div className="circle-clipper left">
            <div className="circle"></div>
          </div><div className="gap-patch">
            <div className="circle"></div>
          </div><div className="circle-clipper right">
            <div className="circle"></div>
          </div>
        </div>
      </div>
    );
  }
  return null;
};


export default Loading;
