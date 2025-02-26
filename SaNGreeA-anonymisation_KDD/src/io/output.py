import sys
import os

out_dir = '../output/'


def outputCSV(clusters, outfile):
    # Check if the directory exists, if not, create it
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        
    out_string = "age, birth_country_mother, marital_stat\n"
    for cluster in clusters:
        out_string += cluster.toString()

    csvOutput = open(out_dir + outfile, 'w')
    csvOutput.write(out_string)