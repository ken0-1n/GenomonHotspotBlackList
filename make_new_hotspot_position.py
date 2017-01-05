import sys

in_file = sys.argv[1]

def check_mismatch_per_sample(depth_list, var_list, in_mis, in_num):
    sample_num = 0
    count = 0
    for i, depth in enumerate(depth_list):
        variant = var_list[i]
        if depth > 20:
            sample_num += 1
            if float(variant) != 0:
                mis = float(variant)/float(depth)
                if mis > float(in_mis) :
                    count += 1
    return ((float(count)/sample_num) > float(in_num))

header_flg = True
with open(in_file, "r") as f:
    for line in f:
        if header_flg:
            header_flg = False
            continue
        F = line.rstrip('\n').split('\t')
        misRate = float(F[11])
        misRate_p = float(F[12])
        misRate_n = float(F[13])
        depth_p_list = F[14].split(',')
        var_p_list = F[15].split(',')
        depth_n_list = F[16].split(',')
        var_n_list = F[17].split(',')
        if check_mismatch_per_sample(depth_p_list,var_p_list, 0.05, 0.06) \
          or check_mismatch_per_sample(depth_n_list,var_n_list, 0.05, 0.06):

            print F[0] +"\t"+ F[1] +"\t"+ F[2] +"\t"+ F[3] +"\t"+ F[4]

        elif misRate_p > 0.01 \
          or misRate_n > 0.01:
        # elif check_mismatch_per_sample(depth_p_list,var_p_list, 0.15, 0.03) \
        #   or check_mismatch_per_sample(depth_n_list,var_n_list, 0.15, 0.03):

            print F[0] +"\t"+ F[1] +"\t"+ F[2] +"\t"+ F[3] +"\t"+ F[4]

