
import src 
import src.io.csvInput_KDD as csv
import src.io.output as out
import catGenHierarchy as CGH
import rangeGenHierarchy as RGH
import nodeCluster as CL
import globals as GLOB

KDD_csv = 'data/KDD_train_subset.csv'
adj_list_csv = 'data/KDD_graph.csv'
genh_dir = 'data/gen_hierarchies/'


def prepareGenHierarchiesObject(dataset):
    # Prepare categorical generalization hierarchies
    genh_country = CGH.CatGenHierarchy('birth_country_mother', genh_dir + 'BirthCountryGH.json')
    genh_marital = CGH.CatGenHierarchy('marital_stat', genh_dir + 'MaritalStatusGH.json')

    # Prepare the age range generalization hierarchy
    min = float('inf')
    max = float('-inf')

    # We have to set the age range before instantiating it's gen hierarchy
    for idx in dataset:
        idx_age = float(dataset[idx].get('age'))
        min = idx_age if idx_age < min else min
        max = idx_age if idx_age > max else max
    print("Found age range of: [" + str(min) + ":" + str(max) + "]")
    genh_age = RGH.RangeGenHierarchy('age', min, max)

    # Let's create one central object holding all required gen hierarchies
    # to pass around to node clusters during computation
    gen_hierarchies = {
        'categorical': {
            'birth_country_mother': genh_country,
            'marital_stat': genh_marital
        },
        'range': {
            'age': genh_age
        }
    }


    return gen_hierarchies


def main():
    print("Starting SaNGreeA algorithm...")

    ## Prepare io data structures
    KDDs = csv.readKDD(KDD_csv)
    adj_list = csv.readAdjList(adj_list_csv)
    gen_hierarchies = prepareGenHierarchiesObject(KDDs)


    ## Main variables needed for SaNGreeA
    clusters = [] # Final output data structure holding all clusters
    best_candidate = None # the currently best candidate by costs
    added = {} # dict containing all nodes already added to clusters


    ## MAIN LOOP
    for i, node in enumerate(KDDs):
        if i % 1000 == 0:  # Print every 100th node
            print(f"Processing node {i}")
        
        if node in added and added[node] == True:
            continue

        # Initialize new cluster with given node
        cluster = CL.NodeCluster(node, KDDs, adj_list, gen_hierarchies)

        # Mark node as added
        added[node] = True

        ## SaNGreeA inner loop - Find nodes that minimize costs and
        ## add them to the cluster since cluster_size reaches k
        while len(cluster.getNodes()) < GLOB.K_FACTOR:
            best_cost = float('inf')
            for candidate, v in ((k, v) for (k, v) in KDDs.items() if k > node):
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

    out.outputCSV(clusters, 'KDD_anonymized.csv')


if __name__ == '__main__':
    main()
