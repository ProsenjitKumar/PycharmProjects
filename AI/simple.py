import tensorflow as tf
import pandas as pd

COLUMN_NAMES = [
    'SepalLength',
    'SepalWidth',
    'PetalLength',
    'PetalWidth',
    'Species'
]

# Import training dataset
training_dataset = pd.read_csv('iris_training.csv', names=COLUMN_NAMES, header=0)
train_x = training_dataset.iloc[:, 0:4]
train_y = training_dataset.iloc[:, 4]

# Import testing dataset
test_dataset = pd.read_csv('iris_test.csv', names=COLUMN_NAMES, header=0)
test_x = test_dataset.iloc[:, 0:4]
test_y = test_dataset.iloc[:, 4]
