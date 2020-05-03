def handler(event, context):
    response = {}
    response['statusCode'] = 200
    response['body'] = 'hello world!'
    return response
