import json

from utils import *


def get_feature(author_id, paper_id):
    p_a = paper_author_data[(paper_author_data['PaperId'] == paper_id)]

    coauthors = dict_coauthor[str(author_id)]
    score = 0
    for _, row in p_a.iterrows():
        if str(row.AuthorId) in coauthors:
            score += coauthors[str(row.AuthorId)]
    feature = [score, sum(coauthors.values()), p_a.shape[0]]
    # print(feature)
    return feature


if __name__ == '__main__':
    print('extra data loading...')
    dict_coauthor = json.load(open(os.path.join(DATASET_PATH, 'coauthor.json')))
    paper_author_data = pd.read_csv(os.path.join(DATASET_PATH, 'PaperAuthor.csv'))
    print('extra data loaded.')

    # print(get_feature(178042, 1145678))
    # print(get_feature(1094224, 995295))
    # exit(0)

    process_bar = pyprind.ProgPercent(len(data_x))
    features = []
    for x in data_x:
        process_bar.update()
        features.append(get_feature(*x))
    pd.to_pickle(features, 'features6.pickle')
