import logo from './logo.svg';
import AnimatedNumber from "react-animated-numbers";
import React from "react";
import './App.css';

function App() {
  const [number, setNumber] = React.useState(1000);
  
  setInterval(() => setNumber(number + 1), 1000);

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
        <label htmlFor="value">Number Difference</label>
        <AnimatedNumber
          fontStyle={{ fontFamily: "Nunito", fontSize: 40 }}
          animateToNumber={number}
          includeComma
          transitions={(index) => ({type: "spring", duration: index})}
          config={{ tension: 50, friction: 40 }}
          onStart={() => console.log("onStart")}
          onFinish={() => console.log("onFinish")}
          animationType={"calm"}
        />
        </div>
    </div>
  );
}

export default App;
