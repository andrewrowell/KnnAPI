import boto3
import time
from sklearn.neighbors import KNeighborsClassifier

def handler(event, context):

    # Get flower data from dynamodb.
    dynamodb = boto3.resource('dynamodb')
    flowertable = dynamodb.Table('iris_data')
    response = flowertable.scan()
    data = response['Items']

    # This handles pagination from DynamoDB.
    while response.get('LastEvaluated'):
        response = flowertable.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    # Input and output data sets to train the KNN classifier.
    x_train = []
    y_train = []

    for row in data:
        x = [row['petal_length'],row['petal_width'],row['sepal_length'],row['sepal_width']]
        x_train.append(x)
        y_train.append(row['species'])

    # K Nearest Neighbors Classifier
    # Arbitrarily chose three neighbor configuration.
    n = KNeighborsClassifier(n_neighbors=3)
    n.fit(x_train, y_train)

    # Build the input data from the event parameters.
    x_test = [[event['petal_length'],event['petal_width'],event['sepal_length'],event['sepal_width']]]

    # Make the prediction.
    y_test = n.predict(x_test)

    # Return it in the response.
    response = {}
    response['statusCode'] = 200
    response['body'] = str(y_test[0])

    return response
