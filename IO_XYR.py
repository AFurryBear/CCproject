import os
import nibabel as nib

import scipy.io as sio
import json

#get a df, [vertice_id,label_id]
#label.gii
def load_label(filepath):
    return nib.load(filepath).darrays[0].data

#nifti
def load_nifti(filepath):
    return nib.load(filepath).get_fdata()


def load_mat(filepath,varName):
    return sio.loadmat(filepath)[varName]

def load_file(filepath):
    with open(filepath, 'r') as f:
        file_data=f.read().splitlines()
    return file_data

def load_json(filepath):
    with open(filepath) as f:
        file_data = json.load(f)
    return file_data

def write_json(var,filename):
    with open(filename, 'w') as f:
        json.dump(var, f)


def BN_Atlas_Lobe():
    lobe_L=[range(1,69,2),range(69,125,2),range(125,163,2),range(163,175,2),range(175,189,2),range(189,211,2)]
    lobe_R=[range(2,69,2),range(70,125,2),range(126,163,2),range(164,175,2),range(176,189,2),range(190,211,2)]
    return lobe_L,lobe_R
