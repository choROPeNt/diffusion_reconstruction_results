[![arXiv](https://img.shields.io/badge/arXiv-2211.13497-00ff00.svg)](https://doi.org/10.48550/arXiv.2211.13497) 


# Results of "Conditional diffusion-based microstructure reconstruction"

This repository contains all samples generated in the paper ["Conditional diffusion-based microstructure reconstruction"](https://doi.org/10.48550/arXiv.2211.13497). For training and sampling of the conditional diffusion models the implementation of OpenAI [improved-difusion](https://github.com/openai/improved-diffusion) and ["Improved Denoising Diffusion Probabilistic Models"]( 	
https://doi.org/10.48550/arXiv.2102.09672) was used, respectively.

The following `READDME.md` contains the instructions to vizualize the generated samples. The samples are stored as `*.npz` containing 64 samples the size 256x256x3 `[h,w,c]` for each class and correspdoning model introduced in ["Conditional diffusion-based microstructure reconstruction"](https://doi.org/10.48550/arXiv.2211.13497).

## Prerequisites

- Python3

## Requirements

- numpy >= 1.22.3
- pillow >= 9.1.0
- matplotlib >= 3.5.2


to install all necessary packages and their dependencies please run 
```
python -m pip install -r requirements.txt
```
sometimes you may run 
```
python3 -m pip install -r requirements.txt
```

## Usage
Just to vizualize the sampled microstructures you can set only the `--file=<path-to-file>` argument:
```
python vizualize_samples.py --file=<path-to-file> 
```
If you want to save the samples in ´*.tif´ imagefile format you have to specify the output directory with the argument `--dir=<path-to-save-images>`:

```
python vizualize_samples.py --file=<path-to-file> --dir=<path-to-save-images>
```
## examples
The following table shows selected images from the coresponding sample files and class, respectively.


| class    |     sample file      |  image |
|----------|:-------------:|------:|
| martensite |  left-aligned | ![](examples/martensite.png) |
| biological |    centered   |   ![](examples/biological.png)  |
| FVC60      | right-aligned      |    ![](examples/FVC60.png)  |
