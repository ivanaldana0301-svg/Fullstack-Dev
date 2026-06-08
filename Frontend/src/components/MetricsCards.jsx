import "./MetricsCards.css";

function MetricsCards({ metrics }) {

  return (

    <div className="metrics-container">

      <div className="metric-card">
        <h3>Total Transactions</h3>
        <p>{metrics.total_transactions}</p>
      </div>

      <div className="metric-card">
        <h3>Total Value</h3>
        <p>${metrics.total_value}</p>
      </div>

      <div className="metric-card">
        <h3>Average Value</h3>
        <p>${metrics.avg_value}</p>
      </div>

    </div>
  );
}

export default MetricsCards;