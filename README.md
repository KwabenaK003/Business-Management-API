# Business-Management-API
A FastAPI-based backend for business management, including user management, transactions, and reporting.

## Features

- User registration and authentication with JWT
- Transaction management (income/expense)
- Financial reporting and summaries

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. The application uses SQLite for simplicity. The database file will be created automatically.

3. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

## API Endpoints

- `POST /users/register` - Register a new user
- `POST /users/login` - Login and get access token
- `GET /users/me` - Get current user info
- `PUT /users/me` - Update current user
- `POST /transactions/` - Create a transaction
- `GET /transactions/` - List transactions
- `GET /transactions/{id}` - Get specific transaction
- `PUT /transactions/{id}` - Update transaction
- `DELETE /transactions/{id}` - Delete transaction
- `GET /reports/summary` - Get financial summary
- `GET /reports/monthly?year=2023&month=1` - Get monthly report

## Database

Uses SQLAlchemy with SQLite. Tables are created automatically on startup.