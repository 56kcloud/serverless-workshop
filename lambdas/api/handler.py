import json
from os import environ


def handle(event, context):
    path = event.get('path', '')
    team = environ['TEAM']

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
            'body': json.dumps({"message": f"Hello {team} !"})
        }
    else:
        return {
            'statusCode': 404,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({"message": "Not Found"})
        }
