import React, { Component } from 'react';
import {Link} from 'react-router-dom';

class Nav extends Component {
    constructor(props) {
        super(props)
        this.state = {
        }
    }

    render() {
        var links;
        if(this.props.active === 1){
            links = <div className="Nav-extd">
                        <Link className="Nav-link Nav-link-active" to="/">Home</Link>
                        <a className="Nav-link" href="/#global">Global</a>
                        <a className="Nav-link" href="/#video">Symptoms</a>
                        <a className="Nav-link" href="/#historySearch">History</a>
                        <Link className="Nav-link" to="/about">About me</Link>
                    </div>
        } else if (this.props.active === 2){
            links = <div className="Nav-extd">
                        <Link className="Nav-link" to="/">Home</Link>
                        <a className="Nav-link" href="/#global">Global</a>
                        <a className="Nav-link" href="/#searchInd">India</a>
                        <a className="Nav-link" href="/#video">Symptoms</a>
                        <a className="Nav-link" href="/#historySearch">History</a>
                        <Link className="Nav-link Nav-link-active" to="/about">About me</Link>
                    </div>
        }else{
            links = <div className="Nav-extd">
                <Link className="Nav-link" to="/">Home</Link>
                <a className="Nav-link" href="/#global">Global</a>
                <a className="Nav-link" href="/#searchInd">India</a>
                <a className="Nav-link" href="/#video">Symptoms</a>
                <a className="Nav-link" href="/#historySearch">History</a>
                <Link className="Nav-link" to="/about">About me</Link>
            </div>
        }
        return (
          <div>
                <div className="Nav">
                    <input id="chbox" class="cbox" type="checkbox" />
                    <label for="chbox" className="Nav--label">
                        <div className="Nav--icon">
                            <div className="Nav--icon--line"></div>
                            <div className="Nav--icon--line"></div>
                            <div className="Nav--icon--line"></div>
                            <div className="Nav--icon--line"></div>
                            <div className="Nav--icon--line"></div>
                            <div className="Nav--icon--line"></div>
                            <div className="Nav--icon--line"></div>
                            <div className="Nav--icon--line"></div>
                            <div className="Nav--icon--line"></div>
                        </div>
                        <div className="Nav--cross"> &#10799; </div>
                    </label>
                    
                    {links}
                </div>  
                
          </div>
        );
    }
}

export default Nav