import React from 'react';

import Row from '../layout/Row';
import Col from '../layout/Col';
import Info from '../display/Info';
import Content from '../layout/Content';
import SearchBar from '../layout/SearchBar';
import Container from '../layout/Container';

import { attach, dettach, getSearch } from '../../utils';


export default class Projects extends React.Component {

  state = {
    data: {},
    loading: true
  };

  handleProjs = (projs) => {
    this.setState({data: projs ? projs : {}, loading: false});
  };

  componentWillMount() {
    attach('/projs', this.handleProjs, true);
  }

  componentWillUnmount() {
    dettach('/projs', this.handleProjs, true);
  }

  render() {
    return (
      <Container>
        <SearchBar/>
        <Content>
          <Row>
            <Col>
              <Info {...this.state} filter={getSearch()}/>
            </Col>
          </Row>
        </Content>
      </Container>
    );
  }

}
