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

    pack_name = row.NAME # Name of the pack
    pack_keywords = row.KEYWORDS # Keywords of the pack

    def createFile():
        with open(f'packs/{pack_name}/config.yml', 'a+') as outfile: # Opens packs folder based on variable value.
            yaml.dump_all(
            df.loc[(df['NAME'] == pack_name)].to_dict(orient='records'), # Send keywords to the right pack.
            outfile,
            sort_keys=False,
            indent=4
            )

    def dumpToYamlFunction():
        with open(f'packs/{pack_name}/config.yml', 'r+') as outfile: # Opens packs folder based on variable value.
            documents = list(yaml.load_all(outfile, Loader=yaml.FullLoader))
            for data in documents:
                data['KEYWORDS'] = pack_keywords # Update the keywords.
            outfile.seek(0) # Move position in outfile to front.
            yaml.dump_all(documents, outfile)
            outfile.truncate() # Discards old keywords data.
        outfile.close()

    if pack_name and os.path.exists(f'packs/{pack_name}'): # Check if the pack is available, row.NAME is the pack name.
        dumpToYamlFunction()
    else:
        pathlib.Path(f"packs/{pack_name}").mkdir()
        createFile()
        print(f'{pack_name} was made!')