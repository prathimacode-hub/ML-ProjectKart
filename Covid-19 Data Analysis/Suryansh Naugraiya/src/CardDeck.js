import React, { Component } from 'react';
import wearMask from "./image/wear-mask.jpg";
import washHands from "./image/wash-hands.jpg";
import makeDistance from "./image/make-distance.jpg";

class CardDeck extends Component {

    render() {
        return (
            <div className="image-deck">
                <img className="image-deck--image image-deck--image-1" src={wearMask} alt="wearMask"/>
                <img className="image-deck--image image-deck--image-2" src={washHands} alt="washHands"/>
                <img className="image-deck--image image-deck--image-3" src={makeDistance} alt="makeDistance"/>
            </div>
        );
    }
}

export default CardDeck