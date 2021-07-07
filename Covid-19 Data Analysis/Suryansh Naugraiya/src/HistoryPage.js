import React from 'react';
import Nav from './Nav';
import HistorySearch from './HistorySearch';

function HistoryPage() {
    return (
        <div className="history-page">
            <div>
                <Nav></Nav>
            </div>
            <div>
                <HistorySearch></HistorySearch>
            </div>
        </div>
    )
}

export default HistoryPage;