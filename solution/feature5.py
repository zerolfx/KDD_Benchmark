from utils import *
import nltk
import re


def get_feature(author_id, paper_id):
    p_a: pd.DataFrame = paper_author_data[paper_author_data['AuthorId'] == author_id]
    p_year = paper_data[paper_data['Id'] == paper_id].iloc[0].Year

    feature = list()
    years = list()
    for _, row in p_a.iterrows():
        paper = paper_data[paper_data['Id'] == row.PaperId]
        if paper.shape[0] == 0:
            continue
        paper = paper.iloc[0]
        if 1800 <= paper.Year <= 2013:
            years.append(paper.Year)
    # print(p_year, years)
    if not years or not 1800 <= p_year <= 2013:
        feature += [0, 0, 0]
    else:
        feature += [1, p_year - min(years), max(years) - p_year]

    return feature


if __name__ == '__main__':
    print('loading extra data...')
    paper_data = pd.read_csv(os.path.join(DATASET_PATH, 'Paper.csv'))
    paper_author_data = pd.read_csv(os.path.join(DATASET_PATH, 'PaperAuthor.csv'))
    print('data loaded.')

    # print(get_feature(1094224, 995295))
    # exit(0)

    process_bar = pyprind.ProgPercent(len(data_x))
    features = []
    for x in data_x:
        process_bar.update()
        features.append(get_feature(*x))
    print(features)
    pd.to_pickle(features, 'features5.pickle')
