import json

def lambda_handler(event, context):
    try:
        message = json.loads(event["body"])
        name = message.get("location", "")
        response = {
            "message": f"File is located at: {name}"
        }
        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
