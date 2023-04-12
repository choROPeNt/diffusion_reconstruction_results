"""
@christian.duereth@tu-dresden.de
"""
import os
import numpy as np
from PIL import Image
from numpy import load
import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse
import fnmatch



def save_images(im,cl,DIR,n):
    print('saving %s' %os.path.join(DIR,cl + '_' + str(n+1).zfill(3) + '.tif'))
    im.save(os.path.join(DIR,cl + '_' + str(n).zfill(3) + '.tif'))

def main():
    parser = argparse.ArgumentParser(description='ShearDetect')
    parser.add_argument('--file', default=None, help='path to *.npz-file')
    parser.add_argument('--file_dir', default=None, help='path to directory with *.npz-files')

    # parser.add_argument('--dir', default=None, help='path for saving images')
    args = parser.parse_args()

    ## get input data
    FILE = args.file
    FILE_DIR  = args.file_dir

    ##=====================
    ## Check User Input
    ##=====================
    if FILE is None and FILE_DIR is not None:
        FILES = list(sorted(fnmatch.filter(os.listdir(FILE_DIR),"*.npz")))
        DIR = FILE_DIR
        print(FILES)
    elif FILE is not None and FILE_DIR is None and os.path.splitext(FILE)[-1] == '.npz':
        FILES = [os.path.basename(FILE)]
        DIR = ROOT_DIR = os.path.dirname(os.path.abspath(FILE))
    else:
        FILES = None
        print("you must provide a *.npz file or a folder containing *.npz files for vizualization")

    ##=====================
    ## Sampling
    ##=====================
    if FILES is not None:
        for sample in FILES:
            print('creating images from %s' %(sample))
            data = load(os.path.join(DIR,sample))

            imgs = [img for img in data['arr_0']]
            cls = [os.path.split(sample)[-1].split('_')[1]]*len(imgs)
            


            rows = int(np.rint(np.sqrt(len(imgs))))
            
            cols = int(np.rint(len(imgs)/rows))

            fig = plt.figure(figsize=(1.25*cols, 1.375*rows))
            


            for n, (img, cl) in enumerate(zip(imgs,cls)):
                if img.shape[2] == 1:
                    img = img.reshape(img.shape[0],img.shape[1])

                ax = fig.add_subplot(rows,cols,n+1)

                im = Image.fromarray(img)

                ax.imshow(im.convert('RGB'),cmap='gray')
                ax.set_title(cl)
                ax.axis('off')
                

                if not os.path.exists(os.path.join(DIR,cl)):
                    os.makedirs(os.path.join(DIR,cl))
                save_images(im,cl,os.path.join(DIR,cl),n)
            # fig.tight_layout(pad=20)
            plt.show()



if __name__ == "__main__":
    main()
