import csv
import pandas
import yaml
import os
from os import path
import pathlib
from yaml.loader import SafeLoader

# Reading whole csv file with panda library.
df = pandas.read_csv('NR_Keywords.csv', sep=';')

for index, row in df.iterrows(): # Iterates the csv file.

    pack_name = str.lower(row['name']) # Name of the pack
    pack_keywords = row['keywords'] # Keywords of the pack


    def dumpToYaml():
        with open(f'packs/{pack_name}/config.yml', 'r+') as outfile: # Opens packs folder based on variable value.
            documents = list(yaml.load_all(outfile, Loader=yaml.FullLoader))
            for data in documents: # Iterate all config.yml
                data['keywords'] = pack_keywords # Update the keywords if changes was made in .csv file.
            outfile.seek(0) # Move position in outfile to front. 
            yaml.dump_all(documents, outfile)
            outfile.truncate() # Discards old keywords data.
        outfile.close()
        

    if pack_name and os.path.exists(f'packs/{pack_name}/config.yml'): # Check if the pack and path is available.
        dumpToYaml()
        print(f'{pack_name} was changed')
    else:
        print(f'{pack_name} was not found')
