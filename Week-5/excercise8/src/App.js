import React from "react";
import Counter from "./Components/Counter";
import CurrencyConverter from "./Components/CurrencyConverter";
import "./App.css";

function App() {
  return (
    <div className="container">
      <Counter />
      <hr />
      <CurrencyConverter />
    </div>
  );
}

export default App;