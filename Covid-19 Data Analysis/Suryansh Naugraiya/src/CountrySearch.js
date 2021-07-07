import React, { PureComponent } from 'react';
import Graph from "./Graph";
import MainList from "./MainList";
import {Consumer} from './Context';

class CountrySearch extends PureComponent {
    constructor(props) {
        super(props)
        this.state = {
            
        }
    }

    render() {
            return(
                <Consumer>
                    {(value) => {
                        const x = value.country;
                        const y = value.countryCases;
                        const z = value.countryDeaths;
                        const a = value.countryTests;
                        return (
                            <div className="country-search">
                                <div className="country-search--intro">
                                    <Graph></Graph>
                                    <div>
                                        <h1>{x.country}</h1>
                                        <h1>Population: <span>{x.population}</span></h1>
                                    </div>
                                </div>
                                <div className="country-search--info">
                                    <div className="wrapper">
                                        <MainList className="MainList" name="New cases" value={y.new} color="rgb(0, 81, 255)"></MainList>
                                        <MainList name="New deaths" value={z.new} color="rgb(20, 50, 184)"></MainList>
                                        <MainList name="Critical cases" value={y.critical} color="rgb(15, 15, 77)"></MainList>
                                    </div>
                                    <div className="wrapper">
                                        <MainList name="Active cases" value={y.active} color="rgb(20, 50, 184)"></MainList>
                                        <MainList name="Recovered" value={y.recovered} color="rgb(15, 15, 77)"></MainList>
                                    </div>
                                    <div className="wrapper">
                                        <MainList name="Total deaths" value={z.total} color="rgb(0, 81, 255)"></MainList>
                                        <MainList name="Total cases" value={y.total} color="rgb(20, 50, 184)"></MainList>
                                        <MainList name="Total tests" value={a.total} color="rgb(15, 15, 77)"></MainList>
                                    </div>
                                </div>
                            </div>
                        );
                    }}
                </Consumer>
            )
    }
}

export default CountrySearch;