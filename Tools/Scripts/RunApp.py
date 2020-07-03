#!/usr/bin/env python3

import os, sys
import Functions


CONFIG = Functions.config()

def installationDir():
    return CONFIG['ci']['app']['setup']['installation_dir'][Functions.osName()]

def appName():
    return CONFIG['tool']['poetry']['name']

def appFileExt():
    return CONFIG['ci']['app']['setup']['file_ext'][Functions.osName()]

def appFullName():
    return f'{appName()}{appFileExt()}'

def appExe():
    d = {
        'macos': f'{appFullName()}/Contents/MacOS/{appName()}',
        'ubuntu': appFullName(), # check this
        'windows': appFullName() # check this
    }
    return d[Functions.osName()]

def appExePath():
    return os.path.join(installationDir(), appName(), appExe())

def runApp():
    try:
        message = f'run {appName()}'
        Functions.run(appExePath(), 'debug')
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

if __name__ == "__main__":
    runApp()
