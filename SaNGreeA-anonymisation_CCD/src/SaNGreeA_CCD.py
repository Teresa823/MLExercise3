import src.io.csvInput_CCD as csv
import src.io.output as out
import catGenHierarchy as CGH
import rangeGenHierarchy as RGH
import nodeCluster as CL
import globals as GLOB

CCD_csv = 'data/CCD_train_subset.csv'
adj_list_csv = 'data/CCD_graph.csv'
genh_dir = 'data/gen_hierarchies/'


def prepareGenHierarchiesObject(dataset):
    
    # Prepare categorical generalization hierarchy
    genh_education = CGH.CatGenHierarchy('EDUCATION', genh_dir + 'educationGH.json')

    # Prepare range generalization hierarchy
    #Limit Bal
    min = float('inf')
    max = float('-inf')

    for idx in dataset:
        idx_limitbal = float(dataset[idx].get('LIMIT_BAL'))
        min = idx_limitbal if idx_limitbal < min else min
        max = idx_limitbal if idx_limitbal > max else max
    print("Found limit bal range of: [" + str(min) + ":" + str(max) + "]")
    genh_limitbal = RGH.RangeGenHierarchy('LIMIT_BAL', min, max)

    # Pay 
    min = float('inf')
    max = float('-inf')

    for idx in dataset:
        idx_payamt = float(dataset[idx].get('PAY_AMT1'))
        min = idx_payamt if idx_payamt < min else min
        max = idx_payamt if idx_payamt > max else max
    print("Found payamt range of: [" + str(min) + ":" + str(max) + "]")
    genh_payamt = RGH.RangeGenHierarchy('PAY_AMT1', min, max)

    # Bill
    min = float('inf')
    max = float('-inf')

    for idx in dataset:
        idx_billamt = float(dataset[idx].get('BILL_AMT1'))
        min = idx_billamt if idx_billamt < min else min
        max = idx_billamt if idx_billamt > max else max
    print("Found billamt range of: [" + str(min) + ":" + str(max) + "]")
    genh_billamt = RGH.RangeGenHierarchy('BILL_AMT1', min, max)

    # Let's create one central object holding all required gen hierarchies
    # to pass around to node clusters during computation
    gen_hierarchies = {
        'categorical': {
            'EDUCATION': genh_education,
        },
        'range': {
            'LIMIT_BAL': genh_limitbal,
            'PAY_AMT1': genh_payamt,
            'BILL_AMT1': genh_billamt
        }
    }

    return gen_hierarchies


def main():
    print("Starting SaNGreeA algorithm...")

    ## Prepare io data structures
    CCDs = csv.readCCD(CCD_csv)
    adj_list = csv.readAdjList(adj_list_csv)
    gen_hierarchies = prepareGenHierarchiesObject(CCDs)


    ## Main variables needed for SaNGreeA
    clusters = [] # Final output data structure holding all clusters
    best_candidate = None # the currently best candidate by costs
    added = {} # dict containing all nodes already added to clusters


    ## MAIN LOOP
    for i, node in enumerate(CCDs):
        if i % 1000 == 0:  # Print every 100th node
            print(f"Processing node {i}")
        
        if node in added and added[node] == True:
            continue

        # Initialize new cluster with given node
        cluster = CL.NodeCluster(node, CCDs, adj_list, gen_hierarchies)

        # Mark node as added
        added[node] = True

        ## SaNGreeA inner loop - Find nodes that minimize costs and
        ## add them to the cluster since cluster_size reaches k
        while len(cluster.getNodes()) < GLOB.K_FACTOR:
            best_cost = float('inf')
            for candidate, v in ((k, v) for (k, v) in CCDs.items() if k > node):
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

    out.outputCSV(clusters, 'CCD_anonymized.csv')


if __name__ == '__main__':
    main()
