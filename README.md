# KnnAPI
Serverless REST API for KNN-based Model Building

Creates an API Gateway endpoint which can be used to add training data, and then query a model.

## Files
* addflower.py - Lambda to add data to DynamoDB.
* knnapi.yml - CFT for api, lambdas, and database.
* s3_setup.sh - creates s3 bucket for lambda zip.
* testflower.py - Lambda to estimate species from a flower's data.
* upload_lambda.sh - zips lambda scripts and uploads them to the s3 bucket.

## To Do
* Finish lambdas
  * Add-training-data lambda - puts data into DynamoDB
  * Query-model lambda - builds KNN model from data in DB, returns result
* Script to test it with the [Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
