import unittest # import na unittests
from flask import json
from app import app  # Import na Flask app

class FlaskRouteTestCase(unittest.TestCase):
    
    def setUp(self):
        # Setiranje na Flask app za unit tests
        self.app = app.test_client()
        self.app.testing = True

    def test_total_spent_valid_user(self):
        # Test #1 - "Testing the /total_spent route for a valid user ID" 
        response = self.app.get('/total_spent/27')  
        self.assertEqual(response.status_code, 200)
        # Checking whether we receive a 200 code - which means the test will be PASS

    def test_total_spent_invalid_user(self):
        # Test #2 - "Testing the /total_spent route for an invalid user ID" 
        response = self.app.get('/total_spent/99999')  # Assuming '99999' is an invalid user ID in our DB
        self.assertEqual(response.status_code, 404)
        # Checking whether we receive a 404 code - which means the user ID is NOT VALID and the 
        #test will be PASS (## Negative Scenario)

    def test_average_spending_by_age(self):
        # Test #3 - "Testing the /average_spending_by_age route" 
        response = self.app.get('/average_spending_by_age')
        self.assertEqual(response.status_code, 200)
        # Checking if the response data structure matches what is expected
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, dict)  # Example check

# Allowing tests to run within the file - > `python test_app.py`
if __name__ == '__main__':
    unittest.main()
