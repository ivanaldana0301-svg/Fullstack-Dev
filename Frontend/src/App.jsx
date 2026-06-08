import { useEffect, useState } from "react";

import { getTransactions, getMetrics } from "./services/api";

import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";

import MetricsCards from "./components/MetricsCards";
import TransactionsTable from "./components/TransactionsTable";
import Charts from "./components/Charts";
import Filter from "./components/Filter";

import "./App.css";

function App() {

  const [transactions, setTransactions] = useState([]);
  const [metrics, setMetrics] = useState({});

  useEffect(() => {

    async function loadData() {

      const transactionsData = await getTransactions();
      const metricsData = await getMetrics();

      setTransactions(transactionsData);
      setMetrics(metricsData);
    }

    loadData();

  }, []);

  return (
    <div>

      <Navbar />

      <Sidebar />

      <div className="main-content">

        <h1>Data Pipeline Dashboard</h1>

        <MetricsCards metrics={metrics} />

        <Filter />

        <Charts data={transactions} />

        <TransactionsTable data={transactions} />

      </div>

    </div>
  );
}

export default App;