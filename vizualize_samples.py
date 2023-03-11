
import os
import numpy as np
from PIL import Image
from numpy import load
import matplotlib.pyplot as plt
import matplotlib as mpl
import argparse




def save_images(im,cl,DIR,n):
    print('saving %s' %os.path.join(DIR,cl + '_' + str(n+1).zfill(3) + '.tif'))
    im.save(os.path.join(DIR,cl + '_' + str(n).zfill(3) + '.tif'))

def main():
    parser = argparse.ArgumentParser(description='ShearDetect')
    parser.add_argument('--file', default=None, help='path to *.npz-file')
    parser.add_argument('--dir', default=None, help='path for saving images')
    args = parser.parse_args()

    ## get input data
    FILE = args.file
    DIR  = args.dir

    if FILE is not None and os.path.splitext(FILE)[-1] == '.npz':
        print('creating images from %s' %os.path.split(FILE)[-1])
        data = load(FILE)

        imgs = [img for img in data['arr_0']]
        cls = [os.path.split(FILE)[-1].split('_')[1]]*len(imgs)
        


        rows = int(np.rint(np.sqrt(len(imgs))))
        
        cols = int(np.rint(len(imgs)/rows))

        fig = plt.figure(figsize=(1.25*cols, 1.375*rows))
        


        for n, (img, cl) in enumerate(zip(imgs,cls)):
            if img.shape[2] == 1:
                img = img.reshape(img.shape[0],img.shape[1])

            ax = fig.add_subplot(rows,cols,n+1)
            im = Image.fromarray(img)

            ax.imshow(im,cmap=mpl.colormaps['binary'])
            ax.set_title(cl)
            ax.axis('off')
            if DIR is not None:
                if not os.path.exists(DIR):
                    os.makedirs(DIR)
                save_images(im,cl,DIR,n)
        # fig.tight_layout(pad=20)
        plt.show()

    else:
        print("you must provide a *.npz File for vizualization")

if __name__ == "__main__":
    main()
