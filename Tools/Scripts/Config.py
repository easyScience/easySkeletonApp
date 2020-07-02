#!/usr/bin/env python3

import os, sys
import toml


def config():
    project_fname = 'pyproject.toml'
    project_fpath = os.path.join(os.getcwd(), project_fname)
    return toml.load(project_fpath)

def osName():
    platform = sys.platform
    if platform.startswith('darwin'):
        return 'macos'
    elif platform.startswith('lin'):
        return 'linux'
    elif platform.startswith('win'):
        return 'windows'
    else:
        print("- Unsupported platform '{0}'".format(platform))
        return None

def key():
    return sys.argv[1]

def getValue(json, element):
    keys = element.split('.')
    rv = json
    for key in keys:
        rv = rv[key]
    if isinstance(rv, dict):
        rv = rv[Functions.osName()]
    return rv

print(getValue(config(), key()))
