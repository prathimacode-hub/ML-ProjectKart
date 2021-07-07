import React, {Component} from 'react'

class Loader extends Component {
   
    render(){
        return (
            <div class="wrapper-loader" style={{ height: `${this.props.height}` }}>
                <div class="square1"></div>
                <div class="square2"></div>
                <div class="square3"></div>
                <div class="square4"></div>
            </div>
        );
    }
}

export default Loader;