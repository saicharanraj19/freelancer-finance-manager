import React from 'react';
import { Link } from 'react-router-dom';

function Dashboard() {
    return (
        <div>
            <h1>Dashboard</h1>
            <Link to="/add-transaction">Add Transaction</Link>
            <Link to="/reports">Reports</Link>
        </div>
    );
}

export default Dashboard;
