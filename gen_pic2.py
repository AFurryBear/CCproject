import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
import PIL.Image as Image
import os
import sys
import IO_XYR as ioxyr
maindir = sys.argv[1]
#template = sys.argv[2]
#type = sys.argv[3]
threshold = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
mask_file = os.path.join(maindir,'../MNICC07mm_XXmask_final_final.nii')
#template_nodes=os.path.join(maindir,'../template_file',template+'_nodes.txt')

def transparent_back(arr):
    img = Image.fromarray(arr).convert('RGBA')
    L, H = img.size
    color_0 = (0, 0, 0, 255)
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img.getpixel(dot)
            color_1 = color_1[0:1] + (0, 0, 255,)
            img.putpixel(dot, color_1)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
            img.putpixel(dot, color_1)
    return img

def gen_pic(label_file,mask_file,threshold):
    arr_ori = np.load(label_file)
    arr=np.zeros(arr_ori.shape())
    arr
    img = transparent_back(arr_ori*255)
    mask = nib.load(mask_file).get_fdata()[131]
    return img,mask

def save_pic(img,mask,template,index,threshold):
    fig, ax = plt.subplots()
    ax.imshow(mask,cmap="gray")
    ax.imshow(img)
    filename = lambda x, y, z:x+'_'+y+'_'+'%03d' % (z*100)+'.png'
    plt.savefig(os.path.join(maindir,'../HCP_group/picture',filename(template, index, threshold)), dpi=1500)


if __name__=="__main__":
    nodes = ioxyr.load_file(template_nodes)
    for index in nodes:
        for th in threshold:
            label_file = os.path.join(maindir , '../HCP_group/part1_result', template , template + '_' + index + '_CCmask.npy')
            img, mask = gen_pic(label_file, mask_file, th)
            save_pic(img, mask, template, index, th)

#
