import random
import requests

API_ENDPOINT = "https://4j0y67iki7.execute-api.us-east-1.amazonaws.com/v1/flower"

iris_data = open('test_data.csv')

# Remove header
data = iris_data.readlines()[1:]

# Remove newline
data = [x[:-1] for x in data]

data = [x.split(',') for x in data]

for datum in data:
    params = {'sepal_length':datum[0],
    'sepal_width':datum[1],
    'petal_length':datum[2],
    'petal_width':datum[3]}
    species = datum[4]
    r = requests.get(url=API_ENDPOINT, params = params)
    print(r.text[1] == species)
