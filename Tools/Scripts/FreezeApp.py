#!/usr/bin/env python3

import os, sys
import easyTemplateLib, easyAppGui, easyAppLogic
import Functions
from PyInstaller.__main__ import run as pyInstallerMain


CONFIG = Functions.config()

def package_name():
    return CONFIG['tool']['poetry']['name']

def separator():
    return CONFIG['ci']['pyinstaller']['separator'][Functions.osName()]

def mainPyPath():
    return os.path.join(os.getcwd(), package_name(), 'main.py')

def appName():
    return package_name()

def distributionDirPath():
    return os.path.join(os.getcwd(), CONFIG['ci']['project']['subdirs']['distribution'])

def workDirPath():
    return os.path.join(os.getcwd(), CONFIG['ci']['project']['subdirs']['build'])

def projectData():
    return f'{package_name()}{separator()}.'

def easyTemplateLibData():
    return f'{easyTemplateLib.__path__[0]}{separator()}.'

def easyAppLogicData():
    return f'{easyAppLogic.__path__[0]}{separator()}.'

def easyAppGuiData():
    return f'{easyAppGui.__path__[0]}{separator()}.'

def iconPath():
    icon_dir = os.path.join(*CONFIG['ci']['app']['icon']['dir'])
    icon_name = CONFIG['ci']['app']['icon']['file_name']
    icon_ext = CONFIG['ci']['app']['icon']['file_ext'][Functions.osName()]
    icon_path = os.path.join(package_name(), icon_dir, f'{icon_name}{icon_ext}')
    return icon_path

def runPyInstaller():
    try:
        message = 'freeze app'
        pyInstallerMain([
            mainPyPath(),                            # Application main file
            f'--name={appName()}',                   # Name to assign to the bundled app and spec file (default: first script’s basename)
            '--noconfirm',                           # Replace output directory (default: SPECPATH/dist/SPECNAME) without asking for confirmation
            '--clean',                               # Clean PyInstaller cache and remove temporary files before building
            '--windowed',                            # Windows and Mac OS X: do not provide a console window for standard i/o.
            '--onedir',                              # Create a one-folder bundle containing an executable (default)
            '--log-level', 'WARN',                   # LEVEL may be one of DEBUG, INFO, WARN, ERROR, CRITICAL (default: INFO).
            '--distpath', distributionDirPath(),     # Where to put the bundled app (default: ./dist)
            '--workpath', workDirPath(),             # Where to put all the temporary work files, .log, .pyz and etc. (default: ./build)
            f'--add-data={projectData()}',           # Add both project Python and QML source files
            f'--add-data={easyTemplateLibData()}',   # Add easyTemplateLib package
            f'--add-data={easyAppLogicData()}',      # Add easyAppLogic package
            f'--add-data={easyAppGuiData()}',        # Add easyAppGui package
            f'--icon={iconPath()}'                   # Add application icon
            ])
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

if __name__ == "__main__":
    runPyInstaller()
