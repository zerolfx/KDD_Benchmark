from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import cross_validate
import warnings

from utils import *

warnings.simplefilter(action='ignore', category=FutureWarning)


features1 = np.mat(pd.read_pickle('features1.pickle'))
features2 = np.mat(pd.read_pickle('features2.pickle'))
features3 = np.mat(pd.read_pickle('features3.pickle'))
features4 = np.mat(pd.read_pickle('features4.pickle'))
features5 = np.mat(pd.read_pickle('features5.pickle'))
features6 = np.mat(pd.read_pickle('features6.pickle'))
features = np.hstack([features1, features2, features3, features4, features5, features6])


res = cross_validate(RandomForestClassifier(n_estimators=120),
                     features, data_y, cv=10, return_train_score=True, n_jobs=4)
print(np.average(res['train_score']))
