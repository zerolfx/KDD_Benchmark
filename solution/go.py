from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate
import warnings
from utils import *
warnings.simplefilter(action='ignore', category=FutureWarning)


features1 = np.mat(pd.read_pickle('features1.pickle'))
features2 = np.mat(pd.read_pickle('features2.pickle'))
features = np.hstack([features1, features2])


res = cross_validate(RandomForestClassifier(), features, data_y, cv=10, return_train_score=True)
print(np.average(res['train_score']))
