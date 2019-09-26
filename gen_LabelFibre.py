import pandas as pd
import numpy as np
import os
import sys
import IO_XYR as ioxyr

maindir = sys.argv[1]
ljh_result = sys.argv[2]
subj = sys.argv[3]
template = sys.argv[4]

fibre_tri = ioxyr.load_mat(os.path.join(maindir,subj,subj+'_'+ljh_result,subj+'_fibre_tri.mat'),'fibre_tri')

labelL_tri = ioxyr.load_label(os.path.join(maindir,subj,'label',subj+'.L.'+template+'.32K.label.gii'))
labelR_tri = ioxyr.load_label(os.path.join(maindir,subj,'label',subj+'.R.'+template+'.32K.label.gii'))
vertice_L = fibre_tri[:,1]-np.ones(fibre_tri[:,1].shape)
vertice_R = fibre_tri[:,3]-np.ones(fibre_tri[:,3].shape)
fibre_tri[:,2] = labelL_tri[vertice_L.astype('int')]
fibre_tri[:,4] = labelR_tri[vertice_R.astype('int')]
fibre_tri=pd.DataFrame(data=fibre_tri,columns=['fibre_index','vertice_L','label_L','vertice_R','label_R']).astype('int')
fibre_tri.to_csv(os.path.join(maindir,'../mid_file/label_fibre',template,subj+'_'+template+'_label_fibre.csv'),index=False)

if template == 'BN_Atlas':
    L_label = range(1,211,2)
    R_label = range(2,211,2)
elif template == 'HCPMMP':
    L_label = range(181,361)
    R_label = range(1,181)


dic={}
for i in range(len(L_label)):
    tmp = list(fibre_tri.loc[(fibre_tri['label_L'] == L_label[i]) & (fibre_tri['label_R'] == R_label[i]), 'fibre_index'].astype('float'))
    dic['%03d' % (L_label[i]) + '_' + '%03d' % (R_label[i])] = tmp


ioxyr.write_json(dic,os.path.join(maindir,'../mid_file/label_fibre',template,subj+'_'+template+'_label_fibre.json'))
