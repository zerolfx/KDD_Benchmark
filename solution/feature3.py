from utils import *
import textdistance
from fuzzywuzzy import fuzz


def get_feature(author_id, paper_id):
    distance_funcs = [
        textdistance.JaroWinkler(),
        textdistance.Jaccard(),
        textdistance.Levenshtein(),
        fuzz.token_sort_ratio
    ]

    a = author_data[author_data['Id'] == author_id].iloc[0]
    p_a = paper_author_data[(paper_author_data['PaperId'] == paper_id) &
                            (paper_author_data['AuthorId'] == author_id)]
    name_l = [10000 for _ in range(len(distance_funcs))]
    aff_l = [10000 for _ in range(len(distance_funcs))]
    for _, row in p_a.iterrows():
        for i, f in enumerate(distance_funcs):
            name_l[i] = min(name_l[i], f(a.Name, row.Name))
            aff_l[i] = min(aff_l[i], f(str(a.Affiliation), str(row.Affiliation)))

    feature = name_l + aff_l
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
    pd.to_pickle(features, 'features3.pickle')
