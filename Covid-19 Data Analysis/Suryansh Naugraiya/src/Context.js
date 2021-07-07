import React, { Component } from 'react';
import axios from 'axios';
const Context = React.createContext();
const countryUrl = "https://covid-193.p.rapidapi.com/statistics?country=";
const historyUrl = "https://covid-193.p.rapidapi.com/history?country=";

export class Provider extends Component {
    constructor(props) {
        super(props)
        this.state = {
                country: {},
                countryCases: {},
                countryDeaths: {},
                countryTests: {},
                historyCases: {},
                historyDeaths: {},
                historyTests: {},
                historyDay: "",
                historyCountry: "",
                searchCountry: this.searchCountry.bind(this),
                searchHistory: this.searchHistory.bind(this)
        };
        this.searchCountry = this.searchCountry.bind(this);
        this.searchHistory = this.searchHistory.bind(this);
    }
    async searchCountry(name){
        const url = countryUrl + name;
        let response = await axios.get(url, {
                "headers":{
                    "Connection": "keep-alive",
                    "Content-Type": "application/octet-stream",
                    "x-rapidapi-host": "covid-193.p.rapidapi.com",
                    "x-rapidapi-key": "ad4e14ea14msh55df9c099167609p18d035jsnac57a282719d",
                    "useQueryString": true
                }
                });
        let toStore = response.data.response;
        this.setState({
            country : toStore[0],
            countryCases : toStore[0].cases,
            countryDeaths : toStore[0].deaths,
            countryTests : toStore[0].tests
        });
    }
    async searchHistory(country, date){
        const url = historyUrl + country + "&day=" + date;
        let res = await axios.get(url, {
                "headers":{
                    "Connection": "keep-alive",
                    "Content-Type": "application/octet-stream",
                    "x-rapidapi-host": "covid-193.p.rapidapi.com",
                    "x-rapidapi-key": "ad4e14ea14msh55df9c099167609p18d035jsnac57a282719d",
                    "useQueryString": true
                }
                });
        let toStore = res.data.response;
        this.setState({
            historyCases: toStore[0].cases,
            historyDeaths: toStore[0].deaths,
            historyTests: toStore[0].tests,
            historyDay: toStore[0].day,
            historyCountry: toStore[0].country
        });
    }

    render() {
        return (
            <Context.Provider value={this.state} >
                {this.props.children}
            </Context.Provider>
        );   
    }
}

export const Consumer = Context.Consumer;
export default Context;