import os
import pandas as pd
import numpy as np
import pyprind

CWD = os.path.dirname(os.path.dirname(__file__))
DATASET_PATH = os.path.join(CWD, 'data', 'dataset')


def load_train_data(file):
    x, y = [], []
    with open(file) as f:
        for line in f.read().splitlines()[1:]:
            cols = line.split(',')
            for t in cols[1].split():
                x.append((int(cols[0]), int(t)))
                y.append(1)
            for t in cols[2].split():
                x.append((int(cols[0]), int(t)))
                y.append(0)
    return x, y


print('loading data...')
data_x1, data_y1 = load_train_data(os.path.join(DATASET_PATH, 'train_set', 'Train.csv'))
data_x2, data_y2 = load_train_data(os.path.join(DATASET_PATH, 'valid_set', 'Valid.gold.csv'))
data_x = data_x1 + data_x2
data_y = data_y1 + data_y2
print('data loaded.')
