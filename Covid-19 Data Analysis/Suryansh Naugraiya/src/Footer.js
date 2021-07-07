import React from 'react';
import logo from './image/cvirus-icon-lg.png';
import { Link } from 'react-router-dom';

function Footer() {
    return (
        <div className="footer">
            <div className="footer--icon">
                <img src={logo} alt="logo"/>
                <h1 className="logo-name">Covisafe</h1>
            </div>
            <div className="footer--content">
                <div className="footer--content-links">
                    <a href="#">Contact</a>
                    <a href="#">Donate</a>
                    <Link to="/about">About me</Link>
                    <a href="/#top">Go to top</a>
                </div>
                <div className="footer--content-text">
                    This website is built by <b>Akshit Khare</b>. You can get the available code for this website on this <a href="https://github.com/akshit2511/covid19-live" target="_blank">Github repo</a> . You can use the code but do not claim it as your own.
                </div>
            </div>
        </div>
    )
}

export default Footer