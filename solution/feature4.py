from utils import *


def get_feature(author_id, paper_id):
    def f(s):
        ss = ''
        for w in s.split():
            ss += w[0]
        return ss

    a = author_data[author_data['Id'] == author_id].iloc[0]
    p_a = paper_author_data[(paper_author_data['PaperId'] == paper_id) &
                            (paper_author_data['AuthorId'] == author_id)]
    feature = list()

    for _, row in p_a.iterrows():
        if f(row.Name) == f(a.Name):
            feature.append(1)
            break
    else:
        feature.append(0)
    return feature


if __name__ == '__main__':
    print('loading extra data...')
    author_data = pd.read_csv(os.path.join(DATASET_PATH, 'Author.csv'))
    paper_author_data = pd.read_csv(os.path.join(DATASET_PATH, 'PaperAuthor.csv'))
    process_bar = pyprind.ProgPercent(len(data_x))
    print('extra data loaded.')
    # print(get_feature(178042, 1145678))
    # exit(0)
    features = []
    for x in data_x:
        process_bar.update()
        features.append(get_feature(*x))
    pd.to_pickle(features, 'features4.pickle')
