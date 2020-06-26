import boto3
import time
from sklearn.neighbors import KNeighborsClassifier

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    flowertable = dynamodb.Table('iris_data')

    response = flowertable.scan()
    data = response['Items']

    # Handle pagination
    while response.get('LastEvaluated'):
        response = flowertable.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    event['petal_length']

    x_train = []
    y_train = []

    for row in data:
        x = [row['petal_length'],row['petal_width'],row['sepal_length'],row['sepal_width']]
        x_train.append(x)
        y_train.append(row['species'])

    # Arbitrarily chosen ML configuration.
    n = KNeighborsClassifier(n_neighbors=3)
    n.fit(x_train, y_train)

    x_test = [[event['petal_length'],event['petal_width'],event['sepal_length'],event['sepal_width']]]

    response = {}
    response['statusCode'] = 200

    # Is this line necessary?
    data[0].pop('id')

    response['body'] = str(n.predict(x_test)[0])
    return response
