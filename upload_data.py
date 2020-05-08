import random
import requests

random.seed(42)

TRAIN_RATIO = 0.8
API_ENDPOINT = "https://byb2xandqc.execute-api.us-east-1.amazonaws.com/v1/flower"

iris_data = open('iris_data.csv')

# Remove header
data = iris_data.readlines()[1:]

# Remove newline
data = [x[:-1] for x in data]

# Encode species
data = [x.replace('setosa','0') for x in data]
data = [x.replace('versicolor','1') for x in data]
data = [x.replace('virginica','2') for x in data]

data = [x.split(',') for x in data]

random.shuffle(data)

length = len(data)

for i in range(int(length*TRAIN_RATIO)):
    print("uploading " + str(i + 1) + " out of " + str(int(length*TRAIN_RATIO)))
    datum = data[i]
    params = {'sepal_length':datum[0],
    'sepal_width':datum[1],
    'petal_length':datum[2],
    'petal_width':datum[3],
    'species':datum[4]}
    requests.post(url=API_ENDPOINT, params = params)
test_data = open('test_data.csv', 'w')
test_data.write("sepal_length,sepal_width,petal_length,petal_width,species")
for i in range(int(length*TRAIN_RATIO), length):
    test_data.write(','.join(data[i]) + "\n")
test_data.close()
