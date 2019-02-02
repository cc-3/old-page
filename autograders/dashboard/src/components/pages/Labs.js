import React from 'react';

import Info from '../display/Info';
import Content from '../layout/Content';
import SearchBar from '../layout/SearchBar';
import Container from '../layout/Container';

import { auth } from '../../firebase';
import { attach, dettach, getSearch } from '../../utils';


export default class Labs extends React.Component {

  state = {
    loading: true,
    data: {},
    uid: undefined
  };

  handleLabs = (labs) => {
    this.setState({data: labs ? labs : {}, loading: false});
  };

  componentWillMount() {
    this.setState({uid: auth.currentUser.uid});
    attach(`/labs/${auth.currentUser.uid}`, this.handleLabs);
  }

  componentWillUnmount() {
    dettach(`/labs/${this.state.uid}`, this.handleLabs);
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
