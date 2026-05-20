# AussieBankOps

A beginner DevOps-style banking API project built with Flask and SQLite.

## Features
- Flask web API
- Health check endpoint
- Account creation endpoint
- Transfer endpoint
- SQLite database
- GitHub version control

## Project structure
- `app.py` - main Flask application
- `requirements.txt` - Python dependencies
- `README.md` - project documentation
- `bank.db` - SQLite database file

## How to run
```bash
cd C:\AussieBankOps
.venv\Scripts\activate
python app.py
```

Open in browser:
- http://127.0.0.1:5000/
- http://127.0.0.1:5000/health

## API endpoints

### GET /
Returns:
- `AussieBankOps is running`

### GET /health
Returns JSON:
```json
{
  "status": "healthy"
}
```

### POST /account/create
Creates a new account.

Example JSON body:
```json
{
  "name": "Sairam",
  "balance": 1000
}
```

### POST /transfer
Transfers money between accounts.

Example JSON body:
```json
{
  "from_account": 1,
  "to_account": 2,
  "amount": 200
}
```

## Why I built this
I built this project as a portfolio project to practice:
- Python Flask
- SQLite
- Git and GitHub
- API design
- beginner DevOps workflow