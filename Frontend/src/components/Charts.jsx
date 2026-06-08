import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

function Charts({ data }) {
  return (
    <BarChart width={700} height={300} data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="transaction_id" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="transaction_value_usd" />
    </BarChart>
  );
}

export default Charts;