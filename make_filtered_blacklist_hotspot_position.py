import sys

in_database = sys.argv[1]
# black_list = sys.argv[2]
black_list = "output/TCGA_all.black_list"

data_hash = {}
with open(black_list, "r") as f:
    for line in f:
        F = line.rstrip('\n').split('\t')
        key = F[0] +"\t"+ F[1] +"\t"+ F[2] +"\t"+ F[3] +"\t"+ F[4]
        data_hash[key] = 1

with open(in_database, "r") as f:
    for line in f:
        F = line.rstrip('\n').split('\t')
        key = F[0] +"\t"+ F[1] +"\t"+ F[2] +"\t"+ F[3] +"\t"+ F[4]
        if key not in data_hash:
            print line.rstrip('\n')

