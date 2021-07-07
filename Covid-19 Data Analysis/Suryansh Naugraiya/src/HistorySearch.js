import React, { PureComponent } from 'react';
import Graph from "./Graph";
import MainList from "./MainList";
import { Consumer } from './Context';

class HistorySearch extends PureComponent {
    constructor(props) {
        super(props)
        this.state = {

        }
    }

    render() {
        return (
            <Consumer>
              {(val)=> {
                  let cases= val.historyCases;
                  let deaths= val.historyDeaths;
                  let tests= val.historyTests;
                  let day= val.historyDay;
                  let name= val.historyCountry;
                  return(
                      <div className="country-search">
                          <div className="country-search--intro " id="history-search-main">
                            <div className="history-search">
                                  <h1>{name}</h1>
                                  <h1>Till <span>{day}</span></h1>
                            </div>
                          </div>
                          <div className="country-search--info">
                              <MainList className="MainList" name="New cases" value={cases.new} color="rgb(0, 81, 255)"></MainList>
                              <MainList className="MainList" name="New deaths" value={deaths.new} color="rgb(0, 81, 255)"></MainList>
                              <MainList className="MainList" name="Total deaths" value={deaths.total} color="rgb(20, 50, 184)"></MainList>
                              <MainList className="MainList" name="Total cases" value={cases.total} color="rgb(15, 15, 77)"></MainList>
                              <MainList className="MainList" name="Total tests " value={tests.total} color="rgb(15, 15, 77)"></MainList>
                          </div>
                      </div>
                  )
              }}
            </Consumer>
        )
    }
}

export default HistorySearch;