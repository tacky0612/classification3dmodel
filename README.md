# Classification3dmodel

<img src="https://raw.githubusercontent.com/tacky0612/classification3dmodel/master/figure/fig1.png" title="Architecture">


This is a Jupyter notebook for classifying 3DCAD models using CNN.
I am using Keras as a framework.

# Requirement
```
Keras  2.2.4
tensorboard 1.9.0     
tensorflow  1.9.0     
tensorflow-gpu  1.10.0
numpy 1.14.5
matplotlib  3.0.0 
scikit-learn  0.20.0
tqdm  4.26.0
```

# How to use
- 3DCAD models data download  
  ModelNet10/40 downlod  
  ```
  $ git clone https://github.com/tacky0612/classification3dmodel.git
  $ cd classification3dmodel
  $ bash get_modelnet.sh
  ```
  
- Convert 3DCAD model to voxels  
  Please run "make_npy_file.ipynb" with Jupyter notebook.  
  It converts the 3D data to voxels.

- Voxel visualization  
  Please run "vis.ipynb" with Jupyter notebook.
  It makes visualization of 3D model.  
  ↓　Like this　↓
  <img src="https://github.com/tacky0612/classification3dmodel/blob/master/figure/fig2.png" title="voxel1">
  <img src="https://github.com/tacky0612/classification3dmodel/blob/master/figure/fig3.png" title="voxel2">

- Classification 3Dmodels
  Please run "Classification_3DSAMPLE.ipynb" with Jupyter notebook.  
  It classifies 3D models.  
  
  ↓　Accuracy　↓  
  
  | ModelNet10 | ModelNet40 | My dataset(3D_SAMPLE) |
  | :---: | :---: | :---: |
  | 90.1% | 86.8% | 97.6% |


# When this does not work
Please check ./config.py  
'DATASET = Modelnet10 or Modelnet40'  
Remove the comment out of this．  
3D_SAMPLE is our own dataset. I can not publish it now.

# P.S.
Forgive me for my poor English... XD

[My twitter](https://twitter.com/tacky0612)  ←　Please contact me if you have any troubles.
