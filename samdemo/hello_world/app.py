import json


def first_lambdaUsingSam(event, context):




    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "AWS is super cool",

            }
        ),
    }
