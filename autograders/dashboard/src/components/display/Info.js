import React from 'react';
import { Link } from 'react-router-dom';

import Emoji from './Emoji';
import Loading from './Loading';
import Row from '../layout/Row';
import Col from '../layout/Col';

import { getDate } from '../../utils';


export default class Info extends React.Component {

  getData = () => {
    const { data, filter } = this.props;
    if (filter !== '') {
      const search = {};
      Object.keys(data).forEach((e) => {
        if (e.toLowerCase().indexOf(filter.toLowerCase()) !== -1)
          search[e] = data[e];
      });
      return search;
    }
    return data;
  };

  getTitle = (text) => {
    const title = text.split('_');
    title[0] = title[0] + ':';
    return title.join(' ');
  };

  getGrade = (info) => {
    const { grade, timestamp } = info;
    const date = timestamp ? getDate(timestamp, true) : '-';
    const style = {color: grade ? (grade > 60 ? '#43a047' : '#e53935') : '#1e88e5'};
    return (
      <div>
        <div className="center">
          <h5>Score: <span style={style}>{grade ? grade : 'pending'}</span></h5>
          <p><small>Last Submit</small></p>
          <p style={{fontWeight: 'bold'}}>{date}</p>
        </div>
      </div>
    );
  };

  renderInfo() {
    const data = this.getData();
    const keys = Object.keys(data);
    if (!this.props.loading && keys.length > 0) {
      return keys.map((e) => {
        return (
          <Col key={e} size="s12 m4 l3">
            <div>
              <div className="card cc-3-panel">
                <div className="card-content">
                  <span className="card-title">
                    <span>{this.getTitle(e)}</span>
                    <Loading loading={data[e].grading} />
                  </span>
                  {this.getGrade(data[e])}
                </div>
                <div className="card-action">
                  <Link
                    to={`/console/${e}`}
                    className="btn waves-effect waves-light green"
                    disabled={data[e].console ? false : true}
                  >
                    <i className="fas fa-terminal left"></i>
                    Output
                  </Link>
                </div>
              </div>
            </div>
          </Col>
        );
      });
    }
    if (this.props.loading)
      return <Emoji text={'Loading...'}/>
    else
      return <Emoji text={'Empty'} />
  }

  render() {
    return (
      <Row>
        {this.renderInfo()}
      </Row>
    );
  }

}
