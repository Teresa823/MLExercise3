import csv

CCD_file_name = '../../data/CCD_train_subset.csv'
adj_list_file_name = '../../data/CCD_graph.csv'


def readCCD(file_name):
    CCD_file = open(file_name, 'r')
    CCD_csv = csv.reader(CCD_file, delimiter=',')

    # ignore the headers
    next(CCD_csv, None)

    # create the dict we need
    CCDs = {}

    for CCD_idx in CCD_csv:
        CCD = CCDs[int(CCD_idx[0])] = {}
        CCD['EDUCATION'] = CCD_idx[3]
        CCD['LIMIT_BAL'] = int(CCD_idx[1])
        CCD['BILL_AMT1'] = int(CCD_idx[12])
        CCD['PAY_AMT1'] = int(CCD_idx[18])
    CCD_file.close()
    return CCDs


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
    print(readCCD(CCD_file_name))
    print(readAdjList(adj_list_file_name))
