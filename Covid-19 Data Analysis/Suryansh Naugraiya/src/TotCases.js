import React, { PureComponent } from 'react'

class TotCases extends PureComponent {
    constructor(props) {
        super(props)
        this.state = {
            
        }
    }

    render() {
        return (
            <div className="tot-cases">
                <h2>Total Cases: <span> 452369896</span></h2>
            </div>
        )
    }
}

export default TotCases