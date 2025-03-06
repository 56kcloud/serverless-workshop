import json
from os import environ


def handle(event, context):
    path = event.get('path', '')
    team = environ.get('TEAM', 'main')

    if path == '/':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({"message": f"Welcome to the API {team}!"})
        }
    elif path == '/hello':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({"message": f"Hello {team}!"})
        }
    else:
        return {
            'statusCode': 404,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({"message": "Not Found"})
        }

if __name__ == "__main__":
    event = {
        "path": "/hello",
        "httpMethod": "GET",
        "headers": {},
        "body": None,
        "isBase64Encoded": False
    }
    print(handle(event, {}))
