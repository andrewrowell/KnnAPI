#TODO run this script on a clean setup to make sure it creates the bucket
# The individual commands worked, but calling ./upload_lambda.sh seemed to
# have trouble with the zip command.
zip lambda.zip addflower.py testflower.py
aws s3 cp lambda.zip s3://knnapi-andrew/lambda.zip
