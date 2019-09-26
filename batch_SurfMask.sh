#!/bin/bash
maindir=/brain/gonggllab/Xiongyirong/HCP_project
subjdir=$maindir/HCP_subject
middir=$maindir/mid_file
codedir=/brain/gonggllab/Xiongyirong/code/HCPCC_project
template1='SurfMask'
for index in $(cat $maindir/template_file/${template1}_nodes.txt|head -300|tail -200)
do
echo "bash $codedir/average_Surfmask.sh $index"|qsub -N xyr_SurfMask_$index -l nodes=1:ppn=2 -q short -o $maindir/log/HCPCC/xyr_SurfMask_out_$index -e $maindir/log/HCPCC/xyr_SurfMask_error_$index
done

