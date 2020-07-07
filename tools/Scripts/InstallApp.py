#!/usr/bin/env python3

import os, sys
import xml.dom.minidom
import dephell_licenses
import Functions


CONFIG = Functions.config()

def distributionDir():
    return CONFIG['ci']['project']['subdirs']['distribution']

def scriptsDir():
    return CONFIG['ci']['project']['subdirs']['scripts']

def appName():
    return CONFIG['tool']['poetry']['name']

def setupName():
    return f"{appName()}{CONFIG['ci']['app']['setup']['file_name_suffix']}"

def setupFileExt():
    return CONFIG['ci']['app']['setup']['file_ext'][Functions.osName()]

def setupFullName():
    return f'{setupName()}{setupFileExt()}'

def setupExe():
    d = {
        'macos': f'{setupFullName()}/Contents/MacOS/{setupName()}',
        'ubuntu': setupFullName(),
        'windows': setupFullName()
    }
    return d[Functions.osName()]

def setupExePath():
    return os.path.join(distributionDir(), setupExe())

def runInstaller():
    try:
        message = f'install {appName()}'
        silent_script = os.path.join(scriptsDir(), CONFIG['ci']['scripts']['silent_install'])
        Functions.installSilently(
            installer=setupExePath(),
            silent_script=silent_script
        )
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

if __name__ == "__main__":
    runInstaller()
