import numpy as np
import IO_XYR as ioxyr
import nibabel as nib
import sys
import os

maindir = sys.argv[1]
opt_type = sys.argv[2]
index = sys.argv[3]
#size = int(sys.argv[4])


def mask_number(sub, threshold=0):
    sub[np.where(sub <= threshold)] = 0
    sub[np.where(sub > threshold)] = 1
    return sub

def gen_mask(sub,threshold=0,method='mask_number'):
    if method=="mask_number":
        sub = mask_number(sub, threshold)
    elif method =="weight_number":
        sub = sub
    return sub

sublist = ioxyr.load_file(os.path.join(maindir,'../sublist.txt'))
index_R,index_C = int(index[0:3]),int(index[4:7])


os.system('mkdir -p ' + os.path.join(maindir ,'../HCP_group/result/part1_result', opt_type))
mask=[]
for subj in sublist:
    filedir = os.path.join(maindir, subj, 'result/part1_result', opt_type, subj + '_' + index + '_CCmask.npy')
    mask.append(gen_mask(np.load(filedir)))
np.save(os.path.join(maindir,'../HCP_group/result/part1_result', opt_type, opt_type+'_'+index+'_CCmask.npy'),np.average(mask, axis=0))

