
import os
import numpy as np
from PIL import Image
from numpy import load
import matplotlib.pyplot as plt
import argparse

def plot_images(img,cls,n):
    im = Image.fromarray(img)
    plt.imshow(im)
    plt.title(cls)
    plt.draw()
    return im


def save_images(im,cl,DIR,n):
    print('saving %s' %os.path.join(DIR,cl + '_' + str(n).zfill(3) + '.tif'))
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


        for n, (img, cl) in enumerate(zip(imgs,cls)):
  
            im = plot_images(img,cl,n)
            if DIR is not None:
                if not os.path.exists(DIR):
                    os.makedirs(DIR)
                save_images(im,cl,DIR,n)
            plt.show()

    else:
        print("you must provide a *.npz File for vizualization")
    
    
    
    


if __name__ == "__main__":
    main()
