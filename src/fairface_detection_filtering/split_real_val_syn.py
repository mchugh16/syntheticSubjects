import os, shutil, csv
from tkinter import filedialog
from tkinter import *

def split_data(group, split, source, destination):
    full_source = source + "/" + group + "/"

    num_real = split["real"]
    num_syn = split["synthetic_training"]
    num_val = split["validation"]

    # do a check to make sure total num of images in split matches actual num
    ideal_total_num = num_real + num_syn + num_val
    images = os.listdir(full_source)
    if ideal_total_num != len(images):
        raise ValueError('Num Images in Splits Do Not Match Actual Num Images')
    print("passed 1st check")

    real = images[0:num_real]
    synthetic_training = images[num_real:num_syn+num_real]
    validation = images[(num_syn+num_real):]

    # do a check to make sure total num of images in splist matches actual num
    total_num_images = len(real) + len(synthetic_training) + len(validation)
    if ideal_total_num != total_num_images:
        print(len(real))
        print(len(synthetic_training))
        print(len(validation))
        raise ValueError('Num Images in Split Groups Do Not Match Actual Intended Splits')
    print("passed 2nd check")

    root = Tk()
    root.withdraw()

    dest_real = destination + "/" + "real" + "/" + group + "/"
    dest_syn = destination + "/" + "synthetic_training" + "/" + group + "/"
    dest_val = destination + "/" + "validation" + "/" + group + "/"

    for filename in os.listdir(full_source):
        if filename in real:
            filename = full_source + filename
            shutil.copy(filename, dest_real)
        elif filename in synthetic_training:
            filename = full_source + filename
            shutil.copy(filename, dest_syn)
        elif filename in validation:
            filename = full_source + filename
            shutil.copy(filename, dest_val)
        else:
            print("file does not exist: " + filename)
    
    # do a last check to make sure total num of images in splits matche num images after splitting
    dest_real_images = os.listdir(dest_real)
    dest_syn_images = os.listdir(dest_syn)
    dest_val_images = os.listdir(dest_val)

    total_dest_images = len(dest_real_images) + len(dest_syn_images) + len(dest_val_images)
    if ideal_total_num != total_dest_images:
        raise ValueError('Num Images in Split Folders Do Not Match Actual Intended Splits')
    print("passed 3rd check")
    

def main():
    # dict with race/gender groups (data dir names) as keys, 
    # and dict with num images to be in real set, synthetic training set, and validation set (40, 40, 20 split) as values
    Easian_f = {
        "real": 1747,
        "synthetic_training": 1748,
        "validation": 874
    }
    Easian_m = {
        "real": 1433,
        "synthetic_training": 1434,
        "validation": 716
    }
    SEasian_f = {
        "real": 1489,
        "synthetic_training": 1490,
        "validation": 745
    }
    SEasian_m = {
        "real": 1382,
        "synthetic_training": 1383,
        "validation": 691
    }
    black_f = {
        "real": 1233,
        "synthetic_training": 1234,
        "validation": 617
    }
    black_m = {
        "real": 993,
        "synthetic_training": 994,
        "validation": 497
    }
    indian_f = {
        "real": 1652,
        "synthetic_training": 1653,
        "validation": 826
    }
    indian_m = {
        "real": 1499,
        "synthetic_training": 1500,
        "validation": 750
    }
    latino_f = {
        "real": 1863,
        "synthetic_training": 1864,
        "validation": 931
    }
    latino_m = {
        "real": 1555,
        "synthetic_training": 1556,
        "validation": 778
    }
    midE_f = {
        "real": 731,
        "synthetic_training": 732,
        "validation": 365
    }
    midE_m = {
        "real": 1336,
        "synthetic_training": 1337,
        "validation": 669
    }
    white_f = {
        "real": 1940,
        "synthetic_training": 1940,
        "validation": 970
    }
    white_m = {
        "real": 1861,
        "synthetic_training": 1862,
        "validation": 931
    }

    splits = {
        "Easian_f": Easian_f,
        "Easian_m": Easian_m,
        "SEasian_f": SEasian_f,
        "SEasian_m": SEasian_m,
        "black_f": black_f,
        "black_m": black_m,
        "indian_f": indian_f,
        "indian_m": indian_m,
        "latino_f": latino_f,
        "latino_m": latino_m,
        "midE_f": midE_f,
        "midE_m": midE_m,
        "white_f": white_f,
        "white_m":white_m
    }

    source = '../../data/fairface-filtered/'
    destination = '../../data/fairface-filtered-split/'
    # split each gender/race supgroup individually
    for key, value in splits.items():
        print("Working on splitting " + key)
        split_data(key, value, source, destination)



if __name__ == "__main__":
    main()