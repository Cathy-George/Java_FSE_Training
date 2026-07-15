import React from "react";
import ListofPlayers from "./Components/ListofPlayers";
import IndianPlayers from "./Components/IndianPlayers";
import "./App.css";

function App() {

  // Change to false to display IndianPlayers component
  const flag = true;

  if (flag === true) {

    return (
      <div className="container">

        <h1>List of Players</h1>

        <ListofPlayers />

      </div>
    );

  }

  return (
    <div className="container">

      <IndianPlayers />

    </div>
  );

}

export default App;