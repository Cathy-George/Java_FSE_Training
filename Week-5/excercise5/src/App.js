import React from "react";
import CohortDetails from "./components/CohortDetails";

function App() {

    const cohorts = [

        {
            cohortCode: "INTADMDF10 - .NET FSD",
            startDate: "22-Feb-2022",
            currentStatus: "Scheduled",
            coach: "Ashima",
            trainer: "Jojo Jose"
        },

        {
            cohortCode: "ADM21JF014 - Java FSD",
            startDate: "10-Sep-2021",
            currentStatus: "Ongoing",
            coach: "Apoorv",
            trainer: "Elisa Smith"
        },

        {
            cohortCode: "CDBJF21025 - Java FSD",
            startDate: "24-Dec-2021",
            currentStatus: "Ongoing",
            coach: "Ashima",
            trainer: "John Doe"
        }

    ];

    return (

        <div>

            <h1 style={{textAlign:"center"}}>
                Cohorts Details
            </h1>

            {
                cohorts.map((cohort,index)=>

                    <CohortDetails
                        key={index}
                        cohort={cohort}
                    />

                )
            }

        </div>

    );

}

export default App;