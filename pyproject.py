#!/usr/bin/env python3

import os, sys
import toml


def config():
    project_fname = 'pyproject.toml'
    project_fpath = os.path.join(os.getcwd(), project_fname)
    return toml.load(project_fpath)

def keyPath():
    if len(sys.argv) < 2:
        return ''
    path = sys.argv[1]
    if len(sys.argv) > 2:
        os = sys.argv[2].split('-')[0]
        path += '.' + os
    return path

def getValue(d, element):
    keys = element.split('.')
    rv = d
    for key in keys:
        rv = rv[key]
    return rv

if __name__ == "__main__":
    print(getValue(config(), keyPath()))
