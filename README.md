# KnnAPI
Serverless REST API for KNN-based Model Building

Creates an API Gateway endpoint which can be used to add training data, and then query a model.

## To Do
* Create lambdas
  * Add-training-data lambda - puts data into DynamoDB
  * Query-model lambda - builds KNN model from data in DB, returns result
* Create CFT
  * API Gateway
  * DynamoDB table
  * Lambdas
* Script to test it with the [Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
