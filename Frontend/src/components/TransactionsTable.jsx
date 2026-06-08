function TransactionsTable({ data }) {
  return (
    <table border="1">
      <thead>
        <tr>
          <th>ID</th>
          <th>Amount</th>
          <th>Price</th>
          <th>Total USD</th>
          <th>Category</th>
        </tr>
      </thead>

      <tbody>
        {data.map((item) => (
          <tr key={item.transaction_id}>
            <td>{item.transaction_id}</td>
            <td>{item.amount}</td>
            <td>{item.price}</td>
            <td>{item.transaction_value_usd}</td>
            <td>{item.category}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default TransactionsTable;