import React from 'react';
import sizeMe from 'react-sizeme';
import { XAxis, YAxis, VerticalBarSeries, FlexibleXYPlot } from 'react-vis';

import { attach, dettach } from '../../utils';


class BarPlot extends React.Component {

  state = {
    data: []
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

  componentWillMount() {
    attach(`/${this.props.dir}`, this.handleData, true);
  }

  componentWillUnmount() {
    dettach(`/${this.props.dir}`, this.handleData, true);
  }

  render() {
    if (this.state.data.length > 0) {
      const { size, title, color } = this.props;
      const dims = {height: Math.floor(size.width / 2), width: '100%'};
      return (
        <div className="card-panel z-depth-1 hide-on-small-only" style={dims}>
          <h5 className="center title">{title}</h5>
          <FlexibleXYPlot
            xType="ordinal"
            yDomain={[0, 100]}
            margin={{bottom: 70}}
            >
            <VerticalBarSeries color={color} data={this.state.data} />
            <XAxis />
            <YAxis title="Grade" tickSize={10} />
          </FlexibleXYPlot>
        </div>
      );
    }
    return null;
  }

}


export default sizeMe()(BarPlot);
