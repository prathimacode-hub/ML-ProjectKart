import React, { PureComponent } from 'react';
import Loader from './Loader';
import Context from './Context';

class InputText extends PureComponent {
    constructor(props) {
        super(props)
        this.state = {
            country: "",
            isLoading: false
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleClick = this.handleClick.bind(this);
    }
    static contextType = Context;

    handleChange(evt){
        this.setState({
            country: evt.target.value
        })
    }
    async handleClick(evt){
        evt.preventDefault();
        let searchCountry = this.context.searchCountry;
        this.setState({
            isLoading: true
        });
        await searchCountry(this.state.country);
        this.setState({
            isLoading: false
        });
        this.props.history.push("/country");
    }
    render() {
        if(this.state.isLoading){
            return(
                <Loader height="8rem"></Loader>
            )
        }else{
            return (
                <form onSubmit={this.handleClick} className="input-text">
                    <input onChange={this.handleChange} type="text" placeholder={this.props.ph} />
                    <button type="submit"><i class="fas fa-search-location"></i></button>
                </form>
            );
        }
    }
}


export default InputText