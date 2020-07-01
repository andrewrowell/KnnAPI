import boto3
import time

def handler(event, context):

    # This just stores the data in DynamoDB.
    dynamodb = boto3.resource('dynamodb')
    flowertable = dynamodb.Table('iris_data')
    flowertable.put_item(Item={'id':str(time.time()),'petal_length':event['petal_length'],'petal_width':event['petal_width'],'sepal_length':event['sepal_length'], 'sepal_width':event['sepal_width'], 'species':event['species']})
    return {'message': 'success'}
