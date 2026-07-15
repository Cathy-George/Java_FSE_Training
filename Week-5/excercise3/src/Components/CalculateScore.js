import "../Stylesheets/mystyle.css";

const percentToDecimal = (decimal) => {
  return (decimal * 100).toFixed(2) + "%";
};

const calcScore = (total, goal) => {
  return percentToDecimal(total / goal);
};

export function CalculateScore({ Name, School, total, goal }) {
  return (
    <div className="formatstyle">

      <h1>Student Details</h1>

      <div className="Name">
        <b>Name :</b> {Name}
      </div>

      <div className="School">
        <b>School :</b> {School}
      </div>

      <div className="Total">
        <b>Total :</b> {total}
      </div>

      <div className="Score">
        <b>Score :</b> {calcScore(total, goal)}
      </div>

    </div>
  );
}