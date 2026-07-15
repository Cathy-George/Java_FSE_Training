import React, { Component } from "react";
import Greeting from "./Components/Greeting";
import LoginButton from "./Components/LoginButton";
import LogoutButton from "./Components/LogoutButton";
import "./App.css";

class App extends Component {

    constructor(props) {

        super(props);

        this.state = {

            isLoggedIn: false

        };

    }

    handleLogin = () => {

        this.setState({

            isLoggedIn: true

        });

    };

    handleLogout = () => {

        this.setState({

            isLoggedIn: false

        });

    };

    render() {

        let button;

        if (this.state.isLoggedIn) {

            button = <LogoutButton onClick={this.handleLogout} />;

        }
        else {

            button = <LoginButton onClick={this.handleLogin} />;

        }

        return (

            <div className="container">

                <Greeting isLoggedIn={this.state.isLoggedIn} />

                {button}

            </div>

        );

    }

}

export default App;