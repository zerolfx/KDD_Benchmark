from utils import *
import nltk
import re


def get_feature(author_id, paper_id):
    def get_words(paper):
        s = str(paper.Title)
        if not pd.isna(paper.Keyword):
            s += paper.Keyword
        # print(s)
        words = re.split(r'[|\s;,]', s)
        words = [w for w in words if w and w not in nltk.corpus.stopwords.words('english') and not w.isdigit()]
        return words

    p_a: pd.DataFrame = paper_author_data[paper_author_data['AuthorId'] == author_id]
    # print(paper_data[paper_data['Id'] == paper_id].iloc[0])
    kws = get_words(paper_data[paper_data['Id'] == paper_id].iloc[0])

    feature = [len(kws)]
    if p_a.shape[0] == 0:
        feature += [0, 0]
    else:
        cnt = 0
        s = set()
        for _, row in p_a.iterrows():
            paper = paper_data[paper_data['Id'] == row.PaperId]
            if paper.shape[0] == 0:
                continue
            paper = paper.iloc[0]
            _kws = get_words(paper)
            cnt += len(_kws)
            s.update(_kws)
        feature.append(cnt / p_a.shape[0])
        feature.append(len(s.intersection(set(kws))))

    return feature


if __name__ == '__main__':
    print('loading extra data...')
    paper_data = pd.read_csv(os.path.join(DATASET_PATH, 'Paper.csv'))
    paper_author_data = pd.read_csv(os.path.join(DATASET_PATH, 'PaperAuthor.csv'))
    print('data loaded.')

    # print(get_feature(178042, 1145678))
    # c = 0
    # for _, row in paper_data.iterrows():
    #     if pd.isna(row.Keyword):
    #         c += 1
    #     print(_, c)
    # print(c, c / paper_data.shape[0])
    # exit(0)

    process_bar = pyprind.ProgPercent(len(data_x))
    features = []
    for x in data_x:
        process_bar.update()
        features.append(get_feature(*x))
    print(features)
    pd.to_pickle(features, 'features2.pickle')
