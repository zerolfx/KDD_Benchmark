import config
import json
import util


# 在 paperauthor 里面是有噪音的，同一个 (authorid,paperid) 可能出现多次，
# 我做的是把同一个 (authorid,paperid) 对的多个 name 和多个 affiliation 合并起来。例如
# aid, pid, name1, aff1
# aid, pid, name2, aff2
# aid, pid, name3, aff3
# 得到 aid, pid, name1##name2##name3, aff1##aff2##aff3, "##" 为分隔符
def load_paperIdAuthorId_to_name_and_affiliation(PaperAuthor_PATH, to_file):
    d = {}
    data = util.read_dict_from_csv(PaperAuthor_PATH)
    for item in data:
        PaperId = item["PaperId"]
        AuthorId = item["AuthorId"]
        Name = item["Name"]
        Affiliation = item["Affiliation"]

        key = "%s|%s" % (PaperId, AuthorId)
        if key not in d:
            d[key] = {}
            d[key]["Name"] = []
            d[key]["Affiliation"] = []

        if Name != "":
            d[key]["Name"].append(Name)
        if Affiliation != "":
            d[key]["Affiliation"].append(Affiliation)

    t = {}
    for key in d:
        name = "##".join(sorted(d[key]["Name"]))
        affiliation = "##".join(sorted(d[key]["Affiliation"]))

        t[key] = {}
        t[key]["name"] = name
        t[key]["affiliation"] = affiliation

    json.dump(t, open(to_file, "w"))


if __name__ == '__main__':
    load_paperIdAuthorId_to_name_and_affiliation(config.PAPERAUTHOR_FILE, config.PAPERIDAUTHORID_TO_NAME_AND_AFFILIATION_FILE)


