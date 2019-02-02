import React from 'react';

import Row from '../layout/Row';
import Col from '../layout/Col';
import Card from '../display/Card';
import Content from '../layout/Content';
import BarPlot from '../display/BarPlot';
import Container from '../layout/Container';
import ReactResizeDetector from 'react-resize-detector';


const Dashboard = () => (
  <Container>
    <Content>
      <Row>
        <Col>
          <Row>
            <Col size="s12 m4 l3">
              <ReactResizeDetector handleWidth>
                <Card title="Labs" color="red" to="/labs"/>
              </ReactResizeDetector>
            </Col>
            <Col size="s12 m4 l3">
              <ReactResizeDetector handleWidth>
                <Card title="Projects" color="green" to="/projects"/>
              </ReactResizeDetector>
            </Col>
            <Col size="s12 m4 l3">
              <ReactResizeDetector handleWidth>
                <Card title="Token" color="blue" modal trigger="token"/>
              </ReactResizeDetector>
            </Col>
            <Col size="m12 l6">
              <ReactResizeDetector handleWidth>
                <BarPlot dir="labs" title="Labs"/>
              </ReactResizeDetector>
            </Col>
            <Col size="m12 l6">
              <ReactResizeDetector handleWidth>
                <BarPlot dir="projs" title="Projects"/>
              </ReactResizeDetector>
            </Col>
          </Row>
        </Col>
      </Row>
    </Content>
  </Container>
);


export default Dashboard;
