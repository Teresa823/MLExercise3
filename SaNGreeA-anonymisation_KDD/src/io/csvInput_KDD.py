import csv

KDD_file_name = '../../data/KDD_train_subset.csv'
adj_list_file_name = '../../data/KDD_graph.csv'


def readKDD(file_name):
    KDD_file = open(file_name, 'r')
    KDD_csv = csv.reader(KDD_file, delimiter=',')

    # ignore the headers
    next(KDD_csv, None)

    # create the dict we need
    KDDs = {}

    for KDD_idx in KDD_csv:
        KDD = KDDs[int(KDD_idx[0])] = {}
        KDD['age'] = KDD_idx[1]
        KDD['marital_stat'] = KDD_idx[5]
        KDD['birth_country_mother'] = KDD_idx[18]
    KDD_file.close()
    return KDDs

def readAdjList(file_name):
    adj_list_file = open(file_name, 'r')
    adj_list_csv = csv.reader(adj_list_file, delimiter=',')

    # create the dict we need
    adj_list = {}

    for adj_idx in adj_list_csv:
        node = adj_list[int(adj_idx[0])] = adj_idx[1:len(adj_idx)-1]

    adj_list_file.close()
    return adj_list


if __name__ == "__main__":
    print(readKDD(KDD_file_name))
    print(readAdjList(adj_list_file_name))
