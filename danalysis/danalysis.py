#!/usr/bin/env python3
import sys
import os
import argparse
import glob
from typing import Dict, List, Sequence

gconfig = {}

def load_plugins(config=gconfig):
    plugins = glob.glob(os.path.join(config['libpath'], "*.py"))
    __all__ = [ basename(f)[:-3] for f in plugins if isfile(f) and not f.endswith('__init__.py')]

def set_config(**kwargs) -> Dict:
    config = gconfig
    scriptpath = os.path.realpath(__file__)
    scriptdir = os.path.dirname(scriptpath)
    libpath = os.path.join(scripdir, 'lib')
    for key, val in kwargs.items():
        gconfig[key] = val
    if 'libpath' not in gconfig:
        config['libpath'] = libpath
    load_config(config)
    return config


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ifile', required=True,
                        help="Input files", nargs='+')
    args = parser.parse_args()
    return args
def main(args):
    config = set_config()
    print(config)
    print(args)

if __name__ == "__main__":
    print(f"{sys.argv[0]} is called")
    main(argparser())
else:
    print(f"{sys.argv[0]} is imported")
