#!/bin/bash
maindir=/brain/gonggllab/Xiongyirong/HCP_project
subjdir=$maindir/HCP_subject
middir=$maindir/mid_file
codedir=/brain/gonggllab/Xiongyirong/code/HCPCC_project
template1='SurfMask'
index=$1
python3 $codedir/average.py $subjdir 'SurfMask' $index 1
python3 $codedir/average.py $subjdir 'SurfMask' $index 2
python3 $codedir/average.py $subjdir 'SurfMask' $index 3



