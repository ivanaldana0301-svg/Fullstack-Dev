# Full Stack Data Pipeline Dashboard

## Overview

This project started as a way for me to strengthen my skills in Python and Data Analysis, but I intentionally designed it following a production-style architecture to simulate how data moves through a real business environment.

The application extracts data from multiple sources, processes and validates it through an ETL pipeline, stores the results in Parquet format, exposes the information through a FastAPI backend, and finally visualizes key metrics and transactions in a React dashboard.

The goal was to combine Data Engineering, Backend Development, and Frontend Development into a single end-to-end project.

---

## Business Scenario

Imagine a company that receives transaction data from internal systems while also consuming external market information through APIs.

The challenge is to:

- Collect information from multiple sources
- Validate data quality
- Transform raw information into useful business metrics
- Store processed data efficiently
- Provide access through APIs
- Visualize results through an interactive dashboard

This project simulates that workflow from beginning to end.

---

# Architecture

```text
CSV Data Source
       │
       ▼
Extract Layer
       │
       ▼
Transform Layer
       │
       ▼
Quality Validation
       │
       ▼
Parquet Storage
       │
       ▼
FastAPI Backend
       │
       ▼
React Dashboard
```

---

# Tech Stack

## Backend

- Python
- FastAPI
- Pandas
- Requests
- PyArrow
- Uvicorn

## Frontend

- React
- Vite
- Axios
- Recharts

## Data Engineering

- ETL Pipelines
- Data Validation
- Parquet Storage
- API Integration

## Development Tools

- Git
- GitHub
- VS Code

---

# Features

## ETL Pipeline

The application implements a complete ETL process:

### Extract

Data is collected from:

- Local CSV files
- External APIs

### Transform

The pipeline:

- Cleans the data
- Standardizes formats
- Generates business metrics
- Calculates transaction values
- Categorizes transactions

### Load

The processed dataset is stored as:

```text
final_data.parquet
```

Using Parquet allows efficient storage and analytics-ready datasets.

---

# Data Quality Validation

Before storing data, validation rules are executed to ensure:

- No null values exist
- Data types are correct
- Business calculations are valid

This simulates quality checks commonly used in production data pipelines.

---

# FastAPI Backend

The backend exposes REST APIs that provide access to the processed data.

### Endpoints

#### Transactions

```http
GET /transactions/
```

Returns all processed transactions.

#### Metrics

```http
GET /metrics/
```

Returns dashboard KPIs such as:

- Total Transactions
- Total Value
- Average Value

#### Pipeline Execution

```http
POST /pipeline/run
```

Executes the ETL process manually.

#### Health Check

```http
GET /health/
```

Returns service status.

---

# API Documentation

FastAPI automatically generates Swagger documentation.

After running the backend:

```text
http://127.0.0.1:8000/docs
```

---

# React Dashboard

The frontend consumes the backend APIs and displays:

### KPI Cards

- Total Transactions
- Total Value
- Average Value

### Interactive Charts

Built using Recharts.

Visualizes:

- Transaction values
- Distribution of processed data

### Transactions Table

Displays:

- Transaction ID
- Amount
- Price
- Total USD Value
- Category

### Dashboard Layout

The interface includes:

- Navigation Bar
- Sidebar
- Metrics Section
- Charts Section
- Data Table

---

# Project Structure

```text
data_pipeline_fullstack/

├── Backend
│   ├── api
│   ├── pipeline
│   ├── data
│   ├── output
│   └── requirements.txt
│
├── Frontend
│   ├── components
│   ├── services
│   ├── App.jsx
│   └── package.json
│
└── README.md
```

---

# What I Learned

Through this project I gained hands-on experience with:

### Backend Development

- FastAPI
- REST API Design
- Service Architecture
- API Documentation

### Data Engineering

- ETL Design
- Data Validation
- Data Transformation
- Parquet Storage
- API Data Integration

### Frontend Development

- React
- Component-Based Architecture
- API Consumption
- Dashboard Development
- Data Visualization

### Software Engineering

- Project Structure
- Separation of Concerns
- Error Handling
- Modular Design

---

# Running the Project

## Backend

Navigate to the backend folder:

```bash
cd Backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn src.api.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend

Navigate to the frontend folder:

```bash
cd Frontend
```

Install dependencies:

```bash
npm install
```

Start the application:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# Future Improvements

Planned improvements for future versions:

- Docker containers
- PostgreSQL integration
- JWT Authentication
- CI/CD with GitHub Actions
- AWS deployment
- PySpark integration
- Scheduled ETL execution
- Advanced filtering
- Responsive mobile dashboard
- Automated testing with Pytest

---

# About Me

I built this project as part of my transition into software development and data engineering, combining my background in manufacturing operations, process optimization, and data analysis with modern development tools.

My goal was not only to create a dashboard, but to understand how data moves through an entire system—from ingestion and validation to APIs and visualization.

This project represents the type of end-to-end solutions I enjoy building and continuously improving.
