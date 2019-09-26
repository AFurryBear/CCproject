import os
import numpy as np
import sys
import IO_XYR as ioxyr

maindir = sys.argv[1]
subj = sys.argv[2]
template = sys.argv[3]

matfile=os.path.join(maindir,'../mid_file/3CoordAfterReg','CCmsp_'+subj+'_CoordAfterReg.mat')
jsonfile=os.path.join(maindir,'../mid_file/label_fibre',subj+'_'+template+'_label_fibre.json')
template_nodes=os.path.join(maindir,'../template_file',template+'_nodes.txt')

ijkindex=ioxyr.load_mat(matfile,'matVoxIJK')
jsondata=ioxyr.load_json(jsonfile)
nodes = ioxyr.load_file(template_nodes)

for homo in nodes:
    if jsondata[homo]==[]:
        cc_mask=np.zeros((311,260))
    else:
        fibre=[]
        for i in list(map(int,jsondata[homo])):
            fibre.append(ijkindex[i-1])
        ori_img=np.zeros((260,311,260))
        for m in range(len(fibre)):
            i,j,k=fibre[m]
            ori_img[i,j,k]=1+ori_img[i,j,k]
        cc_mask=ori_img[132]

    os.system('mkdir -p '+os.path.join(maindir,subj,'result/part1_result',template))
    np.save(os.path.join(maindir,subj,'result/part1_result',template,subj+'_'+homo+'_CCmask.npy'),cc_mask)
