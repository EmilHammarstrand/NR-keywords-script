import csv
import pandas
from ruamel.yaml import YAML
import os
from os import path
import pathlib
from yaml.loader import SafeLoader
import sys


# Reading whole csv file with panda library.
yaml = YAML()
yaml.width = 4096
df = pandas.read_csv('NR_Keywords.csv', sep=';')

for index, row in df.iterrows(): # Iterates the csv file.

    pack_name = str.lower(row['name']) # Name of the pack
    pack_keywords = row['keywords'] # Keywords of the pack

    def dumpToYaml():
        with open(f'packs/{pack_name}/config.yml', 'r+') as outfile: # Opens packs folder based on variable value.
            documents = yaml.load(outfile)
            documents['keywords'] = pack_keywords
            outfile.seek(0) # Move position in outfile to front. 
            yaml.indent(sequence=4, offset=2)
            yaml.dump(documents, outfile)
        outfile.close()


    if pack_name and os.path.exists(f'packs/{pack_name}/config.yml'): # Check if the pack and path is available.
        dumpToYaml()
        print(f'{pack_name} was changed')
    else:
        print(f'{pack_name} was not found')
