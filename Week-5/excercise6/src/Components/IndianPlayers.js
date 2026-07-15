import React from "react";

function IndianPlayers() {

    const IndianTeam = [
        "Sachin",
        "Dhoni",
        "Virat",
        "Rohit",
        "Yuvraj",
        "Raina"
    ];

    // Destructuring
    const [first, second, third, fourth, fifth, sixth] = IndianTeam;

    // Merge Arrays
    const T20Players = [
        "First Player",
        "Second Player",
        "Third Player"
    ];

    const RanjiPlayers = [
        "Fourth Player",
        "Fifth Player",
        "Sixth Player"
    ];

    const IndianPlayers = [...T20Players, ...RanjiPlayers];

    return (

        <div>

            <h2>Odd Players</h2>

            <ul>
                <li>First : {first}</li>
                <li>Third : {third}</li>
                <li>Fifth : {fifth}</li>
            </ul>

            <hr />

            <h2>Even Players</h2>

            <ul>
                <li>Second : {second}</li>
                <li>Fourth : {fourth}</li>
                <li>Sixth : {sixth}</li>
            </ul>

            <hr />

            <h2>List of Indian Players Merged</h2>

            <ul>

                {
                    IndianPlayers.map((player, index) => (

                        <li key={index}>
                            Mr. {player}
                        </li>

                    ))
                }

            </ul>

        </div>

    );

}

export default IndianPlayers;