import os
import tarfile
from six.moves import urllib
import pandas as pd

HOUSINGURL="https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz"
DATASETPATH="datasets/housing"
def fetch_data(url=HOUSINGURL, dpath=DATASETPATH):
    if not os.path.isdir(dpath):
        os.makedirs(dpath)
    tgz_path = os.path.join(dpath, url.split('/')[-1])
    urllib.request.urlretrieve(url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=dpath)
    housing_tgz.close()

def load_housing_data(dpath=DATASETPATH):
    csv_path = os.path.join(dpath, "housing.csv")
    if not os.path.exists(csv_path):
        fetch_data()
    return pd.read_csv(csv_path)


if __name__ == "__main__":
    housing = load_housing_data()
    print("head()")
    print(housing.head())
    print("info()")
    housing.info()
    print("describe()")
    print(housing.describe())
    print("value_counts()")
    print(housing.ocean_proximity.value_counts())
