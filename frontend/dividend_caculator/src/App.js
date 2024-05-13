import AnimatedNumber from "react-animated-numbers";
import React from "react";
import Axios from "axios";
import './App.css';

function App() {
  const [portfolio, setPortfolio] = React.useState(0);
  
  const [capital, setCapital] = React.useState(0);

  const onCalculate = async () => {
    const res = await Axios.get("http://localhost:3001/nasdaq/appl");
    const dividend = res.data[0].cash_amount;
    setPortfolio(capital * dividend * 180);
  }

  return (
    <div className="App">
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "100vh",
          flexDirection: "column"
        }}
      >
        <label htmlFor="value">Your capital</label>
        <input id="capital" type="number" placeholder="Enter capital" onChange={(e) => setCapital(e.target.value)}></input>
        <AnimatedNumber
          fontStyle={{ fontFamily: "Nunito", fontSize: 40 }}
          animateToNumber={portfolio}
          includeComma
          transitions={(index) => ({type: "spring", duration: index})}
          config={{ tension: 90, friction: 40 }}
          onStart={() => console.log("onStart")}
          onFinish={() => console.log("onFinish")}
          animationType={"calm"}
        />
        <button id="btnCalc" onClick={onCalculate}>Calculate</button>
        </div>
    </div>
  );
}

export default App;
