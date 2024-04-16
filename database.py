import sqlite3
from config import SQL_DATABASE, MONGO_URI
from pymongo import MongoClient, errors
from flask import jsonify

# SQLite connection
def get_sqlite_connection():
    conn = sqlite3.connect(SQL_DATABASE)
    return conn

# MongoDB Setup
client = MongoClient(MONGO_URI)
db = client['users_vouchers']
vouchers_collection = db['vouchers']

# Retrieve total spending of a specific user from SQLite
def get_total_spending(user_id):
    conn = get_sqlite_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT user_info.name, SUM(user_spending.money_spent) AS total_spent
        FROM user_info
        JOIN user_spending ON user_info.user_id = user_spending.user_id
        WHERE user_info.user_id = ?
        GROUP BY user_info.user_id
    """, (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def get_average_spending_by_age():
    conn = get_sqlite_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
    age_range,
    AVG(total_spent) AS avg_spending
FROM (
    SELECT 
        user_info.user_id,
        CASE 
            WHEN user_info.age BETWEEN 18 AND 24 THEN '18-24'
            WHEN user_info.age BETWEEN 25 AND 30 THEN '25-30'
            WHEN user_info.age BETWEEN 31 AND 36 THEN '31-36'
            WHEN user_info.age BETWEEN 37 AND 47 THEN '37-47'
            ELSE '>47'
        END AS age_range,
        SUM(user_spending.money_spent) AS total_spent
    FROM user_info
    JOIN user_spending ON user_info.user_id = user_spending.user_id
    GROUP BY user_info.user_id, age_range
) AS user_totals
GROUP BY age_range;
    """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return {age_range: avg_spending for age_range, avg_spending in results}




def get_eligible_users_from_sqlite():
    conn = get_sqlite_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT user_info.user_id, SUM(user_spending.money_spent) AS total_spending
        FROM user_info
        JOIN user_spending ON user_info.user_id = user_spending.user_id
        GROUP BY user_info.user_id
        HAVING SUM(user_spending.money_spent) > 50000
    """)
    eligible_users = cursor.fetchall()
    cursor.close()
    conn.close()
    return eligible_users

