# Keywords Script

This is a Python script that automates the process of adding keywords to each packs config.yml file. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.


#### Make sure you have python installed on your machine, minimun version is 3.7.1. If not, follow this link [Python Installation](https://realpython.com/installing-python/)
```bash
python --version
```

#### Create a virtual environment and activcate it
```bash
python3 -m venv

source venv/bin/activate
```

#### When inside your venv, install the requirements
```bash
pip install -r requirements.txt
```

#### Now you should be ready to go!

## Usage

1. Change or add keywords in the NR_Keywords.csv file
2. Run the python script
```bash
python3 readCsv.py
```
See your changes inside the packs/ foler.
