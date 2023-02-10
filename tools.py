# 會用到的所有package
import numpy as np
import os
from keras.preprocessing import image
from tqdm import tqdm

def path_to_tensor(img_path):
    '''Converts the image in the given path to a tensor'''
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths):
    '''Converts all the images in the given paths to tensors'''
    list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)

#%%
def label_to_category_dict(path):
    '''Returns a dictionary that maps labels to categories'''
    categories = os.listdir('dogImages/train/')
    label_to_cat = map(lambda x: (int(x.split('.')[0]) - 1, x.split('.')[1]), categories)
    label_to_cat = {label: category for label, category in label_to_cat}
    return label_to_cat
