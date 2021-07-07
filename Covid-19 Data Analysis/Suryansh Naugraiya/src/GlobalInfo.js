import React, { PureComponent } from 'react';
import MainList from './MainList';
import Axios from 'axios';

class GlobalInfo extends PureComponent {
    constructor(props) {
        super(props)

        this.state = {
            globalInfo : {}
        }
    }
    async componentDidMount(){
        let response = await Axios.get("https://api.covid19api.com/summary");
        let toStore = response.data.Global;

        this.setState({
            globalInfo: toStore
        })
    }

    render() {
        let x = this.state.globalInfo;
        return (
            <div className="container global-info" id="global">
                <h1 className="heading-white">MY GLOBAL Destruction</h1>
                <div><MainList color="rgb(0, 81, 255)" name="NEW GLOBAL DEATHS" value={x.NewDeaths} /></div>
                <div><MainList color="rgb(20, 50, 184)" name="NEW GLOBAL CASES" value={x.NewConfirmed} /></div>
                <div><MainList color="rgb(15, 15, 77)" name="TOTAL GLOBAL DEATHS" value={x.TotalDeaths} /></div>
                <div><MainList color="rgb(15, 15, 77)" name="TOTAL GLOBAL CASES" value={x.TotalConfirmed} /></div>
            </div>
        );
    }
}

export default GlobalInfo;