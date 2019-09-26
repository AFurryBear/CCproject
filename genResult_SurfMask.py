import nibabel as nib
import numpy as np
import pandas as pd
import os
import IO_XYR as ioxyr
import sys

maindir = sys.argv[1]
subj = sys.argv[2]
template=sys.argv[3]
nifti_file=os.path.join(maindir,'../MNICC07mm_XXmask_final_final.nii')
matfile=os.path.join(maindir,'../mid_file/3CoordAfterReg','CCmsp_'+subj+'_CoordAfterReg.mat')
if template=="NONE":
    terfile = os.path.join(maindir, '../mid_file/label_fibre', 'HCPMMP', subj + '_HCPMMP_label_fibre.csv')
else:
    terfile = os.path.join(maindir,'../mid_file/label_fibre',template,subj+'_'+template+'_label_fibre.csv')

stanCC=ioxyr.load_nifti(nifti_file)
i_index,j_index=np.where(stanCC[131]>0)

tex_L,tex_R = nib.load(os.path.join(maindir,'../L.tex.gii')),nib.load(os.path.join(maindir,'../R.tex.gii'))
label_L,label_R = ioxyr.load_label(os.path.join(maindir,'../S1200.L.HCPMMP.32K.label.gii')),ioxyr.load_label(os.path.join(maindir,'../S1200.R.HCPMMP.32K.label.gii'))

ijk_native=ioxyr.load_mat(matfile,'matVoxIJK')
ijk_index=pd.DataFrame(data=ijk_native,index=list(range(1,len(ijk_native)+1)))

fibre_tri=pd.read_csv(terfile).astype('int')

cc_dic={}
cc_voxel=[]

for m in range(len(i_index)):
    key=str('%03d' %i_index[m])+'_'+str('%03d' %j_index[m])
    cc_voxel.append(key)
    fibre_index=ijk_index[(ijk_index[0]==132) & (ijk_index[1]==i_index[m]) & (ijk_index[2]==j_index[m])].index
    cc_dic[key]=set(fibre_index)&set(fibre_tri['fibre_index'])
fibre_tri=fibre_tri.set_index('fibre_index')
length=[]
for voxel in cc_voxel:
    tex_l,tex_r = np.zeros(np.size(tex_L.darrays[0].data), dtype='float32'), np.zeros(np.size(tex_R.darrays[0].data), dtype='float32')
    for fibre_index in cc_dic[voxel]:
        if template=="NONE":
            tex_l[fibre_tri.loc[fibre_index, 'vertice_L']] = 1 + tex_l[fibre_tri.loc[fibre_index, 'vertice_L']]
            tex_r[fibre_tri.loc[fibre_index, 'vertice_R']] = 1 + tex_r[fibre_tri.loc[fibre_index, 'vertice_R']]
        else:
            vert_L=fibre_tri[fibre_tri.label_L == fibre_tri.loc[fibre_index, 'label_L']].vertice_L
            tex_l[vert_L]=1+tex_l[vert_L]
            vert_R=fibre_tri[fibre_tri.label_R == fibre_tri.loc[fibre_index, 'label_R']].vertice_R
            tex_r[vert_R]=1+tex_r[vert_R]
    tex_l[np.where(label_L==0)[0]],tex_r[np.where(label_R==0)[0]] = 0,0

    os.system('mkdir -p '+os.path.join(maindir,subj,'result/part2_result',template))
    tex_L.darrays[0].data,tex_R.darrays[0].data=tex_l,tex_r

    nib.save(tex_L,os.path.join(maindir , subj , 'result/part2_result' ,template, subj + '_' + voxel + '_L.tex.gii'))
    nib.save(tex_R,os.path.join(maindir , subj , 'result/part2_result' ,template, subj + '_' + voxel + '_R.tex.gii'))