from .utils import *


def get_feature(author_id, paper_id):
    a = author_data[author_data['Id'] == author_id]
    p_a = paper_author_data[(paper_author_data['PaperId'] == paper_id) &
                            (paper_author_data['AuthorId'] == author_id)]
    feature = list()
    feature.append((p_a.Name == a.iloc[0].Name).any())
    feature.append((p_a.Affiliation == a.iloc[0].Affiliation).any())
    feature.append(p_a.shape[0])
    return feature


if __name__ == '__main__':
    author_data = pd.read_csv(os.path.join(DATASET_PATH, 'Author.csv'))
    paper_author_data = pd.read_csv(os.path.join(DATASET_PATH, 'PaperAuthor.csv'))
    process_bar = pyprind.ProgPercent(len(data_x))
    features = []
    for x in data_x:
        process_bar.update()
        features.append(get_feature(*x))
    pd.to_pickle(features, 'features1.pickle')
