#!/usr/bin/env python3

import os, sys
import Functions


BRANCH = sys.argv[1]
CONFIG = Functions.config()

def appName():
    return CONFIG['tool']['poetry']['name']

def distributionDir():
    return CONFIG['ci']['project']['subdirs']['distribution']

def setupName():
    app_version = CONFIG['tool']['poetry']['version']
    setup_os = CONFIG['ci']['app']['setup']['os'][Functions.osName()]
    setup_arch = CONFIG['ci']['app']['setup']['arch'][Functions.osName()]
    return f'{appName()}_{setup_os}_{setup_arch}_v{app_version}'

def zipFileSuffix():
    if BRANCH != 'master':
        return f'_{BRANCH}'
    return ''

def source():
    setup_file_ext = CONFIG['ci']['app']['setup']['file_ext'][Functions.osName()]
    setup_exe_path = os.path.join(distributionDir(), f'{setupName()}{setup_file_ext}')
    return setup_exe_path

def destination():
    setup_zip_name = f'{setupName()}{zipFileSuffix()}.zip'
    setup_zip_path = os.path.join(distributionDir(), setup_zip_name)
    return setup_zip_path

def zip():
    Functions.zip(source(), destination())

if __name__ == "__main__":
    zip()
