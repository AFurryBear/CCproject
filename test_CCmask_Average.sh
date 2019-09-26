#!/bin/bash
maindir=/brain/gonggllab/Xiongyirong/HCP_project
subjdir=$maindir/HCP_subject
middir=$maindir/mid_file
codedir=/brain/gonggllab/Xiongyirong/code/HCPCC_project

template2='HCPMMP'
for index in $(cat $maindir/template_file/${template2}_nodes.txt)
do
echo "python3 $codedir/average_CCmask.py $subjdir 'HCPMMP' $index"|qsub -N xyr_CCMask_$index -l nodes=1:ppn=2 -q short -o $maindir/log/HCPCC/xyr_CCMask_out_$index -e $maindir/log/HCPCC/xyr_CCMask_error_$index

done

template3='BN_Atlas'
for index in $(cat $maindir/template_file/${template3}_nodes.txt)
do
echo "python3 $codedir/average_CCmask.py $subjdir 'BN_Atlas' $index"|qsub -N xyr_CCMask_$index -l nodes=1:ppn=2 -q short -o $maindir/log/HCPCC/xyr_CCMask_out_$index -e $maindir/log/HCPCC/xyr_CCMask_error_$index

done

#template4='LOBES'
#for index in $(cat $maindir/template_file/${template4}_nodes.txt)
#do
#python3 $codedir/average_CCmask.py $subjdir 'LOBES' $index
#done
