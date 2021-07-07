import React, { PureComponent } from 'react';
import Loader from './Loader';
import Context from './Context';

class History extends PureComponent {
    constructor(props) {
        super(props)
        this.state = {
            country: "",
            date: "",
            isLoading: false
        }
        this.handleChange=this.handleChange.bind(this);
        this.handleSubmit=this.handleSubmit.bind(this);
    }
    static contextType = Context;
    handleChange(e){
        this.setState({
            [e.target.name] : e.target.value
        });
    }
    async handleSubmit(e){
        e.preventDefault();
        let searchHistory = this.context.searchHistory;
        this.setState({
            isLoading: true
        });
        console.log("true");
        await searchHistory(this.state.country, this.state.date);
        this.setState({
            isLoading: false
        })
        console.log("false");
        this.props.history.push("/history");
    }
    hasOneDigit(d){
        if(d.toString().length === 1){
            return true;
        }else{
            return false;
        }
    }

    render() {
        let day,month, toShow;
        let d = new Date();
        let dayInit = d.getDate();
        if(this.hasOneDigit(dayInit)){
            day = "0"+dayInit;
        }else{
            day = dayInit;
        }
        let monthInit = d.getMonth()+1;
        if (this.hasOneDigit(monthInit)) {
         month = "0" + monthInit;
        } else {
            month = monthInit;
        }
        let year = d.getFullYear();
        let today = year+"-"+month+"-"+day;

        if(this.state.isLoading){
            return(
                <Loader height="60rem"></Loader>
            )
        }else{
            return(
                <div className="history" id="historySearch">
                    <h1 className="heading-sec"> History</h1>
                    <form onSubmit={this.handleSubmit} className="history-form">
                        <input
                            className="history-form--date"
                            type="date"
                            min="2020-05-01"
                            placeholder="date"
                            max={today}
                            onChange={this.handleChange}
                            name="date" />

                        <input
                            className="history-form--text"
                            type="text"
                            placeholder="Country name"
                            onChange={this.handleChange}
                            name="country" />

                        <button className="history-form--button" type="submit"><i class="fas fa-search"></i></button>
                    </form>
                </div>
            )
        }
    }
}

export default History;