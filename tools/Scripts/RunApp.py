#!/usr/bin/env python3

import os, sys
import Functions


CONFIG = Functions.config()

def installationDir():
    var = CONFIG['ci']['app']['setup']['installation_dir'][Functions.osName()]
    return Functions.environmentVariable(var, var)

def appName():
    return CONFIG['tool']['poetry']['name']

def appFileExt():
    return CONFIG['ci']['app']['setup']['file_ext'][Functions.osName()]

def appExePath():
    d = {
        'macos': os.path.join(installationDir(), appName(), appName()+appFileExt(), 'Contents', 'MacOS', appName()),
        'ubuntu': os.path.join(installationDir(), appName(), appName(), appName()+appFileExt()),
        'windows': os.path.join(installationDir(), appName(), appName(), appName()+appFileExt())
    }
    return d[Functions.osName()]

def runApp():
    Functions.printNeutralMessage(f'Installed application exe path: {appExePath()}')
    try:
        message = f'run {appName()}'
        if len(sys.argv) == 1:
            Functions.run(appExePath())
        else:
            if 'test' in sys.argv[1:]:
                Functions.createDir(CONFIG['ci']['project']['subdirs']['screenshots'])
            Functions.run(appExePath(), *sys.argv[1:])
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

if __name__ == "__main__":
    runApp()
