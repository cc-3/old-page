import React from 'react';

import { history } from '../../router';
import { getSearch } from '../../utils';


export default class SearchBar extends React.Component {

  state = {
    search: getSearch()
  };

  handleChange = (e) => {
    const search = e.target.value;
    history.push({...history.location, search: search !== '' ? 's=' + search : ''});
    this.setState({search});
  };

  render() {
    return (
      <nav>
        <div className="nav-wrapper grey darken-4">
          <div className="input-field">
            <input id="search" autoComplete="off" type="search" onChange={this.handleChange} value={this.state.search} />
            <label className="label-icon" htmlFor="search"><i className="material-icons">search</i></label>
            <i className="material-icons">close</i>
          </div>
        </div>
      </nav>
    );
  }

}
