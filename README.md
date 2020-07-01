# KnnAPI
Serverless REST API for KNN-based Model Building

Creates an API Gateway endpoint which can be used to add training data, and then query a model.

Currently set up to use the [Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set).

# Deploying
1. Install aws cli and aws sam cli, and configure your auth credentials.
2. Deploy the CFT with `sam build && sam deploy --guided`

# Using
## Adding a flower to the database
1. Find your API endpoint in the aws console.
![Picture of console](images/endpoint.png)
2. Make a POST http request like `https://<ENDPOINT>/flower?petal_length=14&petal_width=18&sepal_length=15&sepal_width=18&species=0`

## Files
* lambda/addflower.py - Lambda to add data to DynamoDB.
* template.yml - CFT for api, lambdas, and database.
* lambda/testflower.py - Lambda to estimate species from a flower's data.
* iris_data.csv - CSV file of the [Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
* upload_data.py - Python script to upload training data.
* test_data.py - Sends requests to test accuracy of model built from uploaded data.

## To Do
* Generalize beyond Iris data.
