# python_project (Project Overview)

Flask Web (server) Application for User Spending Analysis
Overview
This Flask application provides APIs to analyze user spending data stored in a SQL database. It allows you to retrieve the total spending by a specific user and calculate the average spending by age ranges. Additionally, it demonstrates how to integrate MongoDB for storing users that exceed specific amount of total spending. In that way, the MongoDB can be accessed for getting the user IDs of the users that are eligible for a bonus voucher at the end of the year. As a bonus, this application will send Telegram messages with calculated statistics to the store management and will also have unit tests for the API endpoints.
Prerequisites
Before developing this application, ensure you have the following components set up (and access to):
1.	SQL deployed (SQLite) Database that will be used for getting the user data
2.	MongoDB: Set up a MongoDB database for storing user data (first locally, and when everything works fine, hosted)
3.	DBBrowser (SQLite)
4.	MySQLWorkbench 8.0
5.	Python 3.x
6.	Modules installed:
	pymongo
	sqlalchemy
	mysql-connector-python
	requests
	jsonify
	json --> -->


# API Endpoints

1. API #1  Retrieve Total Spending by User 
- Endpoint: /total_spent/<int:user_id>
- Method: GET
- Description: Retrieves the total spending for a specific user based on their user ID.
- Parameters:
- user_id (integer): The unique user ID for the user.

- Response:
- JSON object containing the user ID and total spending.


2. API #2 Calculate Average Spending by Age Ranges
- Endpoint: /average_spending_by_age
- Method: GET
- Description: Calculates the average spending for different age ranges and sends the results to specific Telegram users.
- Response:
- JSON object containing average spending for age ranges (18-24, 25-30, 31-36, 37-47, >47)


2. Write user data to MongoDB
- Endpoint: /write_to_mongodb
- Method: POST
- Description: This API endpoint allows clients to submit user data that exceeds specific amount of spending in JSON format, which is then inserted into a MongoDB collection.
- Format of the input JSON data (example): 
- {    
      “user_id”: 1,
      “total_spending”: 2000
- }


- Response: 
Upon successful insertion of the user data into the MongoDB collection, the API will return a JSON response with a success message and the HTTP status code 201 Created. If any errors occur during the insertion process, an error message will be returned with the appropriate HTTP status code and details of the error.
