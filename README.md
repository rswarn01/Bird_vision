# Bird_vision

Overview
Project Name is a Django-based RESTful API for managing products in an e-commerce application. It provides endpoints for creating, updating, retrieving, and deleting products, along with user authentication using JWT tokens. Swagger documentation is integrated to facilitate API exploration.

Features:
  1. Create, read, update, and delete (CRUD) operations for products
  2. User registration and JWT-based authentication
  3. Swagger documentation for API exploration
     
Setup:
  1. Clone the Repository: Copy code : git clone https://github.com/your-username/project-name.git
  2. Navigate to the Project Directory: cd project-name
  3. Create and Activate Virtual Environment: python3 -m venv venv , source venv/bin/activate
  4. Install Dependencies: pip install -r requirements.txt
  5. Apply Migrations: python manage.py migrate
     
Start the Development Server: python manage.py runserver
Access the API:Open your web browser and navigate to http://localhost:8000 to access the API endpoints.
Access Swagger Documentation:Navigate to http://localhost:8000/docs/swagger/ in your browser to view the Swagger documentation for API exploration.

Usage
  1. User Registration
  2. Use the /users/create/ endpoint with a POST request to register a new user.
  3. Provide the username and password in the request body
     Token Generation:
  1. Use the /users/token/ endpoint with a POST request to obtain JWT tokens.
  2. Provide the username and password of the registered user in the request body.
     
Accessing Protected Endpoints:
  1. Include the JWT access token in the Authorization header for each protected endpoint.
  2. Set the Authorization type to Bearer Token and paste the access token.
     
You can now access the protected endpoints for product management.
