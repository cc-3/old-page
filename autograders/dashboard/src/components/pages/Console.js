import React from 'react';

import Row from '../layout/Row';
import Col from '../layout/Col';
import Emoji from '../display/Emoji';
import Content from '../layout/Content';
import Container from '../layout/Container';
import Breadcrumb from '../layout/Breadcrumb';

import { auth } from '../../firebase';
import { attach, dettach } from '../../utils';


export default class Console extends React.Component {

  state = {
    loading: true,
    console: '',
    uid: undefined
  };

  title = `   ___       __       _____            __
  / _ |__ __/ /____  / ___/______ ____/ /__ ____
 / __ / // / __/ _ \\/ (_ / __/ _ \`/ _  / -_) __/
/_/ |_\\_,_/\\__/\\___/\\___/_/  \\_,_/\\_,_/\\__/_/

             Machine Structures
     Great Ideas in Computer Architecture


`

  getBreadcrumbs = () => {
    const paths = [];
    const names = [];
    if (this.props.match.params.id.startsWith('lab')) {
      paths.push('/labs');
      names.push('Labs');
    } else {
      paths.push('/projects');
      names.push('Projects');
    }
    paths.push(this.props.history.location.pathname);
    names.push('Console');
    return {paths, names};
  };

  handleConsole = (console) => {
    this.setState({console, loading: false});
  };

  componentWillMount() {
    const id = this.props.match.params.id;
    this.setState({uid: auth.currentUser.uid});
    let path = `projs/${auth.currentUser.uid}/${id}/`;
    if (id.startsWith('lab'))
      path = `labs/${auth.currentUser.uid}/${id}/`;
    attach(path, this.handleConsole);
  }

  componentWillUnmount() {
    const id = this.props.match.params.id;
    let path = `projs/${this.state.uid}/${id}/`;
    if (id.startsWith('lab'))
      path = `labs/${this.state.uid}/${id}/`;
    dettach(path, this.handleConsole);
  }

  renderConsole() {
    if (!this.state.loading && this.state.console) {
      return (
        <pre className="console">
          {this.title}
          {this.state.console.console}
          {`


=> Score ${this.state.console.grade}/100`}
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
        <Breadcrumb {...this.getBreadcrumbs()} />
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
