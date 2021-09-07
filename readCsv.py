import csv
from collections import OrderedDict

import pandas
from ruamel.yaml import YAML
import os
import sys


def add_key_words(document: OrderedDict, pack_keywords: str):
    if pack_keywords:
        keyword_as_yaml_fragment = YAML()
        document['keywords'] = keyword_as_yaml_fragment.seq(pack_keywords.split(', '))

    return document


# Reading whole csv file with panda library.
yaml = YAML()
yaml.width = 4096
df = pandas.read_csv('NR_Keywords.csv', sep=';')
df_without_null_keywords = df[df['keywords'].notnull()]

for index, row in df_without_null_keywords.iterrows():  # Iterates the csv file.
    pack_name = str.lower(row['name'])  # Name of the pack
    pack_keywords = row['keywords']  # Keywords of the pack

    def dump_to_yaml():
        infile = open(f'packs/{pack_name}/config.yml', 'r')
        documents = yaml.load(infile)
        infile.close()

        documents = add_key_words(documents, pack_keywords)

        outfile = open(f'packs/{pack_name}/config.yml', 'w')
        yaml.indent(sequence=4, offset=2)
        yaml.dump(documents, outfile)
        print(yaml.dump(documents, sys.stdout))
        outfile.close()

    if pack_name and os.path.exists(f'packs/{pack_name}/config.yml'):  # Check if the pack and path is available.
        dump_to_yaml()
        print(f'{pack_name} was changed')
    else:
        print(f'{pack_name} was not found')
