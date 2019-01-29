import React from 'react';

import Info from '../display/Info';
import Content from '../layout/Content';
import SearchBar from '../layout/SearchBar';
import Container from '../layout/Container';

import { attach, dettach, getSearch } from '../../utils';


export default class Labs extends React.Component {

  state = {
    loading: true,
    data: {}
  };

  handleLabs = (labs) => {
    this.setState({data: labs ? labs : {}, loading: false});
  };

  componentWillMount() {
    attach('/labs', this.handleLabs, true);
  }

  componentWillUnmount() {
    dettach('/labs', this.handleLabs, true);
  }

  render() {
    return (
      <Container>
        <SearchBar/>
        <Content>
          <Info {...this.state} filter={getSearch()} />
        </Content>
      </Container>
    );
  }

}
