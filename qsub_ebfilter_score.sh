#!/bin/bash
#
#$ -S /bin/bash         # set shell in UGE
#$ -cwd                 # execute at the submitted dir
#$ -e log
#$ -o log
#$ -l s_vmem=32.0G,mem_req=32.0G


export PATH=/home/kchiba/.local/bin:${PATH}

bq=$1
target_file=$2
in_tumor_bam=$3
controlBam_list=$4
output_dir=$5
sample=$6

mkdir -p $output_dir

EBFilter -Q${bq} -f anno -t8 --debug $target_file $in_tumor_bam $controlBam_list $output_dir/${sample}_output.anno

