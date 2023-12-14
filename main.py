import json
from glob import glob
from pprint import pprint
from object_detection.lyft_processing import read_lyft_data

data_folder = "/Users/samet/Documents/data/lyft_data/"
read_lyft_data(data_folder)
files = glob(data_folder + "*.json")

pprint(files)
data_list = []
for file in files:
    with open(file) as f:
        data = json.load(f)
        # pprint(data)
        data_list.append(data)

print()