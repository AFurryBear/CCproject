#!/bin/bash
maindir=/brain/gonggllab/Xiongyirong/HCP_project
subjdir=$maindir/HCP_subject
middir=$maindir/mid_file
mkdir -p $middir/label_fibre/'HCPMMP' $middir/label_fibre/'BN_Atlas'
mkdir -p $maindir/log/HCPCC
for subj in $(ls $subjdir)
do
echo "bash /brain/gonggllab/Xiongyirong/code/HCPCC_project/subject_script.sh $subj"|qsub -N xyr_HCPCC_$subj -l nodes=1:ppn=2 -q short -o $maindir/log/HCPCC/xyr_HCPCC_out_$subj -e $maindir/log/HCPCC/xyr_HCPCC_error_$subj
done
