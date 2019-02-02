import React from 'react';
import { BarChart } from 'react-easy-chart';

import { attach, dettach } from '../../utils';


class BarPlot extends React.Component {

  state = {
    data: [],
    width: 300,
  };

  handleData = (data) => {
    if (data) {
      const plotData = [];
      Object.keys(data).filter((e) => data[e].grade).forEach((e) => {
        plotData.push({x: e.split('_')[0], y: data[e].grade});
      });
      this.setState({data: plotData});
    }
  };

  onResize = (width) => {
    this.setState({width});
  };

  componentWillMount() {
    attach(`/${this.props.dir}`, this.handleData, true);
  }

  componentWillUnmount() {
    dettach(`/${this.props.dir}`, this.handleData, true);
  }

  render() {
    const { title, width } = this.props;
    if (this.state.data.length > 0 && width > 0) {
      return (
        <div className="card-panel z-depth-1 hide-on-small-only" style={{width: '100%'}}>
          <h5 className="center title">{title}</h5>
          <BarChart
            colorBars
            axes
            width={Math.floor(width)}
            height={Math.floor(width / 2.2)}
            yDomainRange={[0, 100]}
            yTickNumber={10}
            interpolate={'cardinal'}
            y2Type="linear"
            lineData={this.state.data}
            data={this.state.data}
          />
        </div>
      );
    }
    return null;
  }

}


export default BarPlot;
