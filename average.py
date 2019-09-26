import numpy as np
import IO_XYR as ioxyr
import nibabel as nib
import sys
import os

maindir = sys.argv[1]
opt_type = sys.argv[2]
index = sys.argv[3]
size = int(sys.argv[4])


def mask_number(sub, threshold=0):
    sub[np.where(sub <= threshold)[0]] = 0
    sub[np.where(sub > threshold)[0]] = 1
    return sub

def index_li(index):
    return list(range(index-size+1,index+size))

def gen_mask(sub,threshold=0,method='mask_number'):
    if method=="mask_number":
        sub = mask_number(sub, threshold)
    elif method =="weight_number":
        sub = sub
    return sub

sublist = ioxyr.load_file(os.path.join(maindir,'../sublist.txt'))
index_R,index_C = int(index[0:3]),int(index[4:7])

if opt_type=='SurfMask':
    for folder_dir in ['HCPMMP','Homo_HCPMMP','BN_Atlas','Homo_BN_Atlas','NONE']:
        os.system('mkdir -p '+os.path.join(maindir,'../HCP_group/result/part2_result',folder_dir,'%03d' % size))
        for hemi in ['L', 'R']:
            all_data=[]
            for subj in sublist:
                sub_data = []
                for r in index_li(index_R):
                    for c in index_li(index_C):
                        filedir = os.path.join(maindir, subj, 'result/part2_result',folder_dir,subj + '_' + str(r) + '_' + str(c) + '_' + hemi + '.tex.gii')
                        if os.path.exists(filedir):
                            label_data=ioxyr.load_label(filedir)
                            label_data.flags.writeable = True
                            sub_data.append(gen_mask(label_data))
                all_data.append(gen_mask(np.sum(sub_data, axis=0)))
            label = nib.load(os.path.join(maindir, '../'+hemi+'.tex.gii'))
            label.darrays[0].data = np.average(all_data, axis=0)
            nib.save(label,os.path.join(maindir,'../HCP_group/result/part2_result', folder_dir,'%03d' % size, 'Group_'+index+'_'+hemi+'.tex.gii'))

else:
    os.system('mkdir -p ' + os.path.join(maindir ,'../HCP_group/result/part1_result', opt_type))
    mask=[]
    for subj in sublist:
        filedir = os.path.join(maindir, subj, 'result/part1_result', opt_type, subj + '_' + index + '_CCmask.npy')
        mask.append(gen_mask(np.load(filedir)))
    np.save(os.path.join(maindir,'../HCP_group/result/part1_result', opt_type, opt_type+'_'+index+'_CCmask.npy'),np.average(mask, axis=0))

