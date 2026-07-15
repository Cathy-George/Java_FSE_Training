import React from "react";
import "./App.css";

function App() {

    const offices = [

        {
            id: 1,
            Name: "DBS",
            Rent: 50000,
            Address: "Chennai"
        },

        {
            id: 2,
            Name: "TCS",
            Rent: 75000,
            Address: "Bangalore"
        },

        {
            id: 3,
            Name: "Infosys",
            Rent: 45000,
            Address: "Hyderabad"
        },

        {
            id: 4,
            Name: "Cognizant",
            Rent: 90000,
            Address: "Kochi"
        }

    ];

    return (

        <div className="container">

            <h1>Office Space , at Affordable Range</h1>

            {

                offices.map((office) => (

                    <div className="card" key={office.id}>

                        <img
                            src="office.webp"
                            alt="Office Space"
                            className="officeImage"
                        />

                        <h2>Name: {office.Name}</h2>

                        <h3
                            style={{
                                color:
                                    office.Rent <= 60000
                                        ? "red"
                                        : "green"
                            }}
                        >
                            Rent Rs. {office.Rent}
                        </h3>

                        <h3>Address: {office.Address}</h3>

                    </div>

                ))

            }

        </div>

    );

}

export default App;