import React from 'react';

import Row from '../layout/Row';
import Col from '../layout/Col';
import Card from '../display/Card';
import Content from '../layout/Content';
import BarPlot from '../display/BarPlot';
import Container from '../layout/Container';


const Dashboard = () => (
  <Container>
    <Content>
      <Row>
        <Col>
          <Row>
            <Col size="s12 m3">
              <Card title="Labs" color="red" to="/labs"/>
            </Col>
            <Col size="s12 m3">
              <Card title="Projects" color="green" to="/projects"/>
            </Col>
            <Col size="s12 m3">
              <Card title="Token" color="blue" modal trigger="token"/>
            </Col>
            <Col size="m12 l6">
              <BarPlot dir="labs" title="Labs" color="#8e24aa" />
            </Col>
            <Col size="m12 l6">
              <BarPlot dir="projs" title="Projects" color="#fdd835 " />
            </Col>
          </Row>
        </Col>
      </Row>
    </Content>
  </Container>
);


export default Dashboard;
