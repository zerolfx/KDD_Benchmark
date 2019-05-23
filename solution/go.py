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
features = [features2, features3, features4, features5, features6]
features_mat = np.hstack(features)
print(features_mat.shape)


res = cross_validate(RandomForestClassifier(n_estimators=100),
                     features_mat, data_y, cv=10, return_train_score=True, n_jobs=4)
print(np.average(res['train_score']))


# clf = RandomForestClassifier(n_estimators=100)
# clf.fit(features_mat[:len(data_x1), :], data_y1)
# yy = clf.predict_proba(features_mat[:len(data_x1), :])
# c = 0
# for i in range(len(data_y1)):
#     c += data_y1[i] == yy[i]
# print(c, c / len(data_y1))

# clf = RandomForestClassifier(n_estimators=100)
# clf.fit(features_mat, data_y)
# pd.to_pickle(clf, 'clf.pickle')
