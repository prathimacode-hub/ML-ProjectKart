import React, {Component} from 'react';
import Header from './Header';
import GlobalInfo from './GlobalInfo';
import Video from './Video';
import History from './History';
import Footer from './Footer';
import Nav from './Nav';

class Home extends Component{
    
    render(){
        return (
            <div className="home">
                <div>
                    <Nav active={1}></Nav>
                </div>
                <div>
                    <Header history={this.props.history} ></Header>
                    <Video></Video>
                    <GlobalInfo></GlobalInfo>
                    <History history={this.props.history}></History>
                    <Footer></Footer>
                </div>
            </div>
        )
    }
}

export default Home;