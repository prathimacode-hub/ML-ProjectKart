import React from 'react';
import Nav from './Nav';
import CountrySearch from './CountrySearch';

function CountryPage() {
    return (
        <div className="country-page">
            <div>
                <Nav></Nav>
            </div>
            <div>
                <CountrySearch></CountrySearch>
            </div>
        </div>
    )
}

export default CountryPage;