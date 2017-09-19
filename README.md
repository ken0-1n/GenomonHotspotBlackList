# GenomonHotspotErrorFilter

This tool made based on EBFilter (https://github.com/Genomon-Project/EBFilter)

Requires
----------

An UGE cluster environment

Dependecy
----------

1 make lists of TCGA normal bam.
```
bash make_list_normal_TCGA.sh
```
2. make your target mutations file (file format is tab separated anno format coordinates "chr \t start \t end \t ref \t alt ").
```
awk -F"   " '{print $1"\t"$2"\t"$3"\t"$4"\t"$5}' ../GenomonHotspotDatabase/results/refGene_hotspot.txt > input/hotspot.anno 
```
3. read counts for TCGA normal bam.
```
run_qsub_ebfilter_score_TCGA.sh
```
4. merge result No 3
```
bash run_make_black_list.sh
```
5. filter hotspot error position
```
python make_filtered_blacklist_hotspot_position.py ../GenomonHotspotDatabase/output/refGene_hotspot.txt > ../GenomonHotspotDatabase/output/refGene_hotspot_filtered_blacklist.txt
```

