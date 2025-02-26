import csv

PID_file_name = '../../data/PID_train_new.csv'
adj_list_file_name = '../../data/PID_graph.csv'


def readPID(file_name):
    PID_file = open(file_name, 'r')
    PID_csv = csv.reader(PID_file, delimiter=',')

    # ignore the headers
    next(PID_csv, None)

    # create the dict we need
    PIDs = {}

    for PID_idx in PID_csv:
        PID = PIDs[int(PID_idx[0])] = {}
        PID['Age'] = int(PID_idx[8])
        PID['BloodPressure'] = PID_idx[3]
        PID['Insulin'] = PID_idx[5]
    PID_file.close()
    return PIDs


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
    print(readPID(PID_file_name))
    print(readAdjList(adj_list_file_name))
