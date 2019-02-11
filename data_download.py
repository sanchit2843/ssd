import wget
import supportlib.gettingdata as getdata
import os
def download(path = None):
    wget.download('http://ufldl.stanford.edu/housenumbers/train_32x32.mat')
    wget.download('http://ufldl.stanford.edu/housenumbers/train.tar.gz')
    if path = None:
        getdata.tarextract(os.getcwd())
    else:
        getdata.tarextract(path)