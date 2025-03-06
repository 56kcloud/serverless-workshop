import unittest
from lambdas.api.handler import handle


class TestHandler(unittest.TestCase):

    def test_root_path(self):
        event = {"path": "/", "httpMethod": "GET"}
        response = handle(event, {})
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], '{"message": "Welcome to the API chaos-monkeys!"}')

    def test_hello_path(self):
        event = {"path": "/hello", "httpMethod": "GET"}
        response = handle(event, {})
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], '{"message": "Hello chaos-monkeys!"}')

    def test_not_found_path(self):
        event = {"path": "/unknown", "httpMethod": "GET"}
        response = handle(event, {})
        self.assertEqual(response['statusCode'], 404)
        self.assertEqual(response['body'], '{"message": "Not Found"}')


if __name__ == "__main__":
    unittest.main()
