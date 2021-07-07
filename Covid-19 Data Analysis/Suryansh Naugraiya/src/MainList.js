import React, { PureComponent } from 'react'

class MainList extends PureComponent {
    constructor(props) {
        super(props)

        this.state = {
            
        }
    }

    render() {
        return (
            <div style={{backgroundColor: `${this.props.color}`}} className="main-list">
                <span className="main-list-name">{this.props.name}:</span>
                <span className="main-list-value">{this.props.value}</span>
            </div>
        )
    }
}

export default MainList