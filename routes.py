from flask import Flask, jsonify, abort, request
from database import get_total_spending 
from database import get_average_spending_by_age 
from database import get_eligible_users_from_sqlite
from database import vouchers_collection


from pymongo import errors

# app = Flask(__name__)

def configure_routes(app):
    print("...") 

    @app.route('/')
    def hello_world():
        return 'Python Course 2 AVRSM'

    @app.route('/total_spent/<int:user_id>', methods=['GET'])
    def total_spent(user_id):
        result = get_total_spending(user_id)
        if result:
            return jsonify({'user_name': result[0], 'total_spent': result[1]})
        else:
            abort(404, description="User ID does not exists in the data base")



    @app.route('/average_spending_by_age', methods=['GET'])
    def calculate_average_spending_by_age():
        data = get_average_spending_by_age()
        return jsonify(data)


    @app.route('/write_to_mongodb', methods=['POST'])
    def write_to_mongodb():
        eligible_users = get_eligible_users_from_sqlite()
        inserted_count = 0
        for user in eligible_users:
            try:
                result = vouchers_collection.insert_one({'user_id': user[0], 'total_spending': user[1]})
                inserted_count += 1
            except errors.PyMongoError as e:
                return jsonify({"error": "Database error", "details": str(e)}), 500
        return jsonify({"message": f"{inserted_count} user(s) data inserted successfully into MongoDB - Vouchers Collection"}), 201


    