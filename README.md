# Performing Loans Dashboard

**Note:** This project is under development.

A reproducible dashboard project for bank loan portfolio management, using anonymized synthetic data generated with Python, stored in PostgreSQL, and visualized in Power BI.

## Features

- Synthetic data generation for clients, managers, accounts, contracts, and measures.
- PostgreSQL database for data storage.
- Power BI integration for analytics and reporting.
- Docker containerization for easy setup and reproducibility.

## Prerequisites

- Docker and Docker Compose
- Power BI Desktop (for visualization)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/l-tiezerin/performing-loans-dashboard.git
   cd performing-loans-dashboard
   ```

2. Build and run with Docker:
   ```
   docker-compose up --build
   ```

3. Generate data (if not automated):
   ```
   docker-compose exec app python src/generate_data.py
   ```

4. Connect Power BI to PostgreSQL (localhost:5432) and import tables.

## Project Structure

- `src/`: Python scripts for data generation.
- `Dockerfile`: App container.
- `docker-compose.yml`: Services (app, postgres).
- `assets/`: Reference materials (not included in repo).

## License

MIT License.