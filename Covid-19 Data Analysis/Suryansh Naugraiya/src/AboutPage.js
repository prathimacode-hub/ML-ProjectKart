import React from 'react';
import Nav from './Nav';
import About from './About';

function AboutPage() {
    return (
        <div className="about-page">
            <div>
                <Nav active={2}></Nav>
            </div>
            <div>
                <About></About>
            </div>
        </div>
    )
}

export default AboutPage;