#TODO run this script on a clean setup to make sure it creates the bucket
aws s3api create-bucket --bucket knnapi-andrew --acl private
./upload_lambda.sh
