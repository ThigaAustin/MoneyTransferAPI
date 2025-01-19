# Money Transfer REST API

A RESTful API for managing accounts and performing money transfers between them. Built using Python, Flask, and SQLite for a simple and lightweight implementation.

---

## **Features**

- Create new accounts with an initial balance.
- Retrieve account details.
- Transfer money between accounts with constraints:
  - No account can have a negative balance.
  - Transfers fail if the source account has insufficient funds or if the transfer amount is invalid.
- Basic security against SQL injection via SQLAlchemy.
- Easily extensible and scalable codebase.

---

## **Table of Contents**

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Endpoints](#endpoints)
  - [Error Handling](#error-handling)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)

---

## **Prerequisites**

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Postman (for API testing)

---

## **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/money-transfer-api.git
   cd money-transfer-api

2. **Create and activate a Virtual Environment**
    python -m venv venv
    venv\scripts\activate

3. **Install Dependencies**
    pip install -r requirements.txt

4. **Run the Application**
    python run.py
    (The application should be accessible at the url http://127.0.0.1:5000 )


## **API Endpoints**
1. **Request Account**
URL: http://127.0.0.1:5000/accounts
Method: POST 
Description: Creates an account with a starting balance

Request Body(Json):
 {
  "name": "string",
  "balance": "float"
}

Response Success:
{
  "id": int,
  "name": "string",
  "balance": float
}

Response (Error- Negative Balance):
{
  "error": "Balance cannot be negative. Please try again"
}

2. **Retrieve Account**
URL: http://127.0.0.1:5000/accounts/'id'
Method: GET
Description: Retrieves the account details using the account ID

Response Success:
{
  "id": int,
  "name": "String",
  "balance": float
}

Response (Error - Account Not found):
{
  "error": "Account not found, try a valid  account ID"
}

3. **Transfer Money**
URL: http://127.0.0.1:5000/transfers
Method: POST
Description: Transfers money from one account to another

Request Body:
{
  "source_account_id": "int",
  "target_account_id": "int",
  "amount": "float"
}

Response Success:
{
  "message": "Transfer successful"
}

Response (Error - Insufficient Funds):
{
  "error": "Insufficient funds, Top up and Try again"
}

Response (Error - Invalid Accounts):
{
  "error": "Invalid account(s)"
}

Response (Error - Invalid Transfer Amount):
{
  "error": "Transfer amount must be greater than zero"
}

## **Testing**
**Using Postman**
1.Open Postman and create requests for each endpoint
2.Input the respective URL in the URL section
3.Use the request body guide provided above to come up with examples for testing.

## **Project Structure**
money-transfer/
├── app/
│   ├── __init__.py         # App initialization and configuration
│   ├── models.py           # Database models for Account and Transfer
│   ├── routes.py           # API route definitions
│   └── database.py         # Database setup and initialization
├── run.py                  # Main entry point to run the Flask app
├── requirements.txt        # Project dependencies
└── README.md               # Documentation

## **Future Enhancements**
Implement user authentication and authorization.
Add support for pagination and filtering on account and transfer lists.
Implement better concurrency handling for large-scale deployments.
Add deployment scripts for cloud platforms like AWS, Azure, or Heroku.

