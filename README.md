# Simple Bank Application

A simple bank application built with Django that allows users to create accounts, deposit and withdraw funds, and view their account balance.

## Features

- User registration and authentication
- Account creation and management
- Deposit and withdrawal transactions
- Account balance display
- Transaction history
- Basic error handling and validation

## Installation

1. Clone the repository:

   ```shell
   $ git clone https://github.com/HustleDanie/Banking-System.git
   $ cd Banking-System
   ```

2. Create and activa te a virtual environment:

   ```shell
   $ python -m venv venv
   $ source venv/bin/activate  # For Linux/Mac
   $ .\venv\Scripts\activate  # For Windows
   ```

3. Install the required dependencies:

   ```shell
   $ pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```shell
   $ python manage.py migrate
   ```

5. Start the development server:

   ```shell
   $ python manage.py runserver
   ```

6. Access the application at `http://localhost:8000` in your postman.

## API Endpoints
Use these API Endpoints were deemed fit:
- `POST /allbanks/api/create-bank/` 
- `POST /useraccount/api/new-account/` 
- `POST /useraccount/api/update-account/` 
- `POST /useraccount/api/login/` 
- `POST /useraccount/api/delete-user/2/` 
- `POST /useraccount/api/user-balance/`



## Contact

If you have any questions or suggestions, feel free to contact me:

- Email: danieluche2018@gmail.com
- Twitter: [@daniehustl](https://twitter.com/daniehustl)

I appreciate your interest in this project!