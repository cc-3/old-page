import React from 'react';
import sizeMe from 'react-sizeme';
import { XYPlot, XAxis, YAxis, VerticalBarSeries } from 'react-vis';

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
      return (
        <div className="card-panel z-depth-1" style={{width: '100%'}}>
          <h5 className="center">{title}</h5>
          <XYPlot
            xType="ordinal"
            width={Math.floor(size.width - 50)}
            height={Math.floor(size.width - 50) / 2}
            yDomain={[0, 100]}
            >
            <VerticalBarSeries color={color} data={this.state.data} />
            <XAxis />
            <YAxis title="Grade" tickSize={10} />
          </XYPlot>
        </div>
      );
    }
    return null;
  }

}


export default sizeMe()(BarPlot)
