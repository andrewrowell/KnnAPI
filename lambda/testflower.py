import boto3
import time


def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    flowertable = dynamodb.Table('iris_data')

    response = flowertable.scan()
    data = response['Items']

    while response.get('LastEvaluated'):
        response = flowertable.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    event['petal_length']
    response = {}
    response['statusCode'] = 200

    data[0].pop('id')

    response['body'] = str(data[0]) + "-" + str(event['petal_length'])
    return response
