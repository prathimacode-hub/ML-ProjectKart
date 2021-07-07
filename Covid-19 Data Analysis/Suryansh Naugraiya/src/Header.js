import React, { Component } from 'react'
import CardDeck from "./CardDeck";
import TotCases from "./TotCases";
import InputText from "./InputText";
import logo from "./image/cvirus-icon-sm.png";


class Header extends Component {
    constructor(props) {
        super(props)
        this.state = {}
    }

    render() {
        return (
            <div className="header" id="top">
                <div className="header-main">
                    <div className="header-main--content">
                        <div className="header-main--content-icon">
                            <img className="logo" src={logo} alt="logo" />
                            <h1 className="logo-name">Covisafe</h1>
                        </div>
                        <div className="header-main--content-text">
                            Hello! I am Covid-19. Follow my progress around the world. Just type the country name
                        </div>
                        <div className="header-main--content-form">
                            <h2>Let's get started!</h2>
                            <InputText history={this.props.history} ph="Country name"></InputText>
                        </div>
                    </div>
                    <div className="header-main--card_deck">
                        <CardDeck></CardDeck>
                    </div>
                </div>
                <div className="gd">
                    <a href="/#global">Checkout my global Destruction &darr;</a>
                </div>
            </div>
        );
    }
}

export default Header