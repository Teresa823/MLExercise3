
import src 
import src.io.csvInput_PID as csv
import src.io.output as out
import catGenHierarchy as CGH
import rangeGenHierarchy as RGH
import nodeCluster as CL
import globals as GLOB

PIDs_csv = 'data/PID_train_new.csv'
adj_list_csv = 'data/PID_graph.csv'
genh_dir = 'data/gen_hierarchies/'


def prepareGenHierarchiesObject(dataset):
    
    # Prepare range generalization hierarchy

    #Age
    min = float('inf')
    max = float('-inf')

    for idx in dataset:
        idx_age = dataset[idx].get('Age')
        min = idx_age if idx_age < min else min
        max = idx_age if idx_age > max else max
    print("Found age range of: [" + str(min) + ":" + str(max) + "]")
    genh_age = RGH.RangeGenHierarchy('Age', min, max)

    # BloodPressure
    min = float('inf')
    max = float('-inf')

    for idx in dataset:
        idx_bloodpressure = float(dataset[idx].get('BloodPressure'))
        min = idx_bloodpressure if idx_bloodpressure < min else min
        max = idx_bloodpressure if idx_bloodpressure > max else max
    print("Found blood pressure range of: [" + str(min) + ":" + str(max) + "]")
    genh_bloodpressure = RGH.RangeGenHierarchy('BloodPressure', min, max)

    # Insulin
    min = float('inf')
    max = float('-inf')

    for idx in dataset:
        idx_insulin = float(dataset[idx].get('Insulin'))
        min = idx_insulin if idx_insulin < min else min
        max = idx_insulin if idx_insulin > max else max
    print("Found insulin range of: [" + str(min) + ":" + str(max) + "]")
    genh_insulin = RGH.RangeGenHierarchy('Insulin', min, max)

    # Let's create one central object holding all required gen hierarchies
    # to pass around to node clusters during computation
    gen_hierarchies = {
        'range': {
            'Age': genh_age,
            'BloodPressure': genh_bloodpressure,
            'Insulin': genh_insulin
        }
    }

    return gen_hierarchies


def main():
    print("Starting SaNGreeA algorithm...")

    ## Prepare io data structures
    PIDs = csv.readPID(PIDs_csv)
    adj_list = csv.readAdjList(adj_list_csv)
    gen_hierarchies = prepareGenHierarchiesObject(PIDs)


    ## Main variables needed for SaNGreeA
    clusters = [] # Final output data structure holding all clusters
    best_candidate = None # the currently best candidate by costs
    added = {} # dict containing all nodes already added to clusters


    ## MAIN LOOP
    for node in PIDs:
        if node in added and added[node] == True:
            continue

        # Initialize new cluster with given node
        cluster = CL.NodeCluster(node, PIDs, adj_list, gen_hierarchies)

        # Mark node as added
        added[node] = True

        ## SaNGreeA inner loop - Find nodes that minimize costs and
        ## add them to the cluster since cluster_size reaches k
        while len(cluster.getNodes()) < GLOB.K_FACTOR:
            best_cost = float('inf')
            for candidate, v in ((k, v) for (k, v) in PIDs.items() if k > node):
                if candidate in added and added[candidate] == True:
                    continue

                cost = cluster.computeNodeCost(candidate)
                if cost < best_cost:
                    best_cost = cost
                    best_candidate = candidate

            cluster.addNode(best_candidate)
            added[best_candidate] = True

        ## We have filled our cluster with k entries, push it to clusters
        clusters.append(cluster)

    print("Successfully built " + str(len(clusters)) + " clusters.")

    out.outputCSV(clusters, 'PID_train_anonymized.csv')


if __name__ == '__main__':
    main()
