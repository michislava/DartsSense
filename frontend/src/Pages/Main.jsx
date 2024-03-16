import React from 'react';
import './Style.css';
import './Animations.css';
import board from '../Assets/BoardReal.png';

function Main() {
    return <div className="relative h-screen bg-gray-100">
    <div className="flying-dart1"></div>
    <div className="flying-dart2"></div>
    <div className="flying-dart3"></div>
    <div className="Board">
      <img src={board} alt="Sample" />
    </div>
    <div className="fadeText">
      <h1>DartsSense</h1>
    </div>
  </div>
  }
  
export default Main;