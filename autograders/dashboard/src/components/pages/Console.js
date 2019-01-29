import React from 'react';

import Row from '../layout/Row';
import Col from '../layout/Col';
import Emoji from '../display/Emoji';
import Content from '../layout/Content';
import Container from '../layout/Container';

import { auth } from '../../firebase';
import { attach, dettach } from '../../utils';


export default class Console extends React.Component {

  state = {
    loading: true,
    console: ''
  };

  handleConsole = (console) => {
    this.setState({console, loading: false});
  };

  componentWillMount() {
    const id = this.props.match.params.id;
    let path = `projs/${auth.currentUser.uid}/${id}/console`;
    if (id.startsWith('lab'))
      path = `labs/${auth.currentUser.uid}/${id}/console`;
    attach(path, this.handleConsole);
  }

  componentWillUnmount() {
    const id = this.props.match.params.id;
    let path = `projs/${auth.currentUser.uid}/${id}/console`;
    if (id.startsWith('lab'))
      path = `labs/${auth.currentUser.uid}/${id}/console`;
    dettach(path, this.handleConsole);
  }

  renderConsole() {
    if (!this.state.loading && this.state.console) {
      return (
        <pre className="console">
          {this.state.console}
        </pre>
      );
    }
    if (this.state.loading)
      return <Emoji text="Loading..."/>
    return <Emoji text="Not Found..."/>
  }

  render() {
    return (
      <Container>
        <Content>
          <Row>
            <Col>
              {this.renderConsole()}
            </Col>
          </Row>
        </Content>
      </Container>
    )
  }

}
