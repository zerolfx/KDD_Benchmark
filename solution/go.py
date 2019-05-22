from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_validate
from utils import *

features1 = np.mat(pd.read_pickle('features1.pickle'))
features2 = np.mat(pd.read_pickle('features2.pickle'))
features = np.hstack((features1, features2))
print(features.shape)


res = cross_validate(GaussianNB(), features, data_y, cv=10, return_train_score=True)
print(np.average(res['train_score']))
