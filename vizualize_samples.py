
import os
import numpy as np
from PIL import Image
from numpy import load
import matplotlib.pyplot as plt

def plot_images():
    pass

def main():
    file = ".//samples//DaEv_256_cond13_300k//samples_biological_64x256x256x3.npz"
    data = load(file)
    print(data)


if __name__ == "__main__":
    main()
