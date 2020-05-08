# KnnAPI
Serverless REST API for KNN-based Model Building

Creates an API Gateway endpoint which can be used to add training data, and then query a model.

Currently set up to use the [Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set).

# Deploying
1. Replace all `knnapi-andrew` with your unique bucket name.
2. Create the bucket with `aws s3api create-bucket --bucket <YOUR BUCKET NAME> --acl private`.
3. Zip the lambda executables with `zip lambda.zip addflower.py testflower.py`.
4. Upload the lambda with `aws s3 cp lambda.zip s3://<YOUR_BUCKET_NAME>/lambda.zip`.
5. Deploy the CFT with `aws cloudformation deploy --template-file knnapi.yml --stack-name knnapi --capabilities CAPABILITY_NAMED_IAM`

# Using
## Adding a flower to the database
1. Find your API endpoint in the aws console.
![Picture of console](images/endpoint.png)
2. Make a POST http request like `https://<ENDPOINT>/flower?petal_length=14&petal_width=18&sepal_length=15&sepal_width=18&species=0`

## Files
* addflower.py - Lambda to add data to DynamoDB.
* knnapi.yml - CFT for api, lambdas, and database.
* s3_setup.sh - creates s3 bucket for lambda zip.
* testflower.py - Lambda to estimate species from a flower's data.
* upload_lambda.sh - zips lambda scripts and uploads them to the s3 bucket.

## To Do
* Finish lambdas
  * Query-model lambda - builds KNN model from data in DB, returns result
* Script to test it with the [Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
