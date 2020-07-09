#!/usr/bin/env python3

import os, sys
import glob
import PySide2, shiboken2
import easyTemplateLib, easyAppGui, easyAppLogic
import Functions
from PyInstaller.__main__ import run as pyInstallerMain


CONFIG = Functions.config()

def appName():
    return CONFIG['tool']['poetry']['name']

def package_name():
    return f'{appName()}App'

def separator():
    return CONFIG['ci']['pyinstaller']['separator'][Functions.osName()]

def mainPyPath():
    return os.path.join(os.getcwd(), package_name(), 'main.py')

def distributionDirPath():
    return os.path.join(os.getcwd(), CONFIG['ci']['project']['subdirs']['distribution'])

def workDirPath():
    return os.path.join(os.getcwd(), CONFIG['ci']['project']['subdirs']['build'])

def projectData():
    return f'{package_name()}{separator()}{package_name()}'

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
        pyproject_py = f'pyproject.py{separator()}.'
        pyproject_toml = f'pyproject.toml{separator()}.'
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
            '--exclude-module', '_tkinter',          # Exclude tcl/tk toolkit
            f'--add-data={projectData()}',           # Add both project Python and QML source files
            f'--add-data={easyTemplateLibData()}',   # Add easyTemplateLib package
            f'--add-data={easyAppLogicData()}',      # Add easyAppLogic package
            f'--add-data={easyAppGuiData()}',        # Add easyAppGui package
            f'--add-data={pyproject_py}',            #
            f'--add-data={pyproject_toml}',          #
            f'--icon={iconPath()}'                   # Add application icon
            ])
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def excludeLibs():
    exclude_files = CONFIG['ci']['pyinstaller']['exclude_libs'][Functions.osName()]
    if len(exclude_files) == 0:
        Functions.printNeutralMessage(f'No libraries to be excluded for {Functions.osName()}')
        return
    try:
        message = 'exclude libraries'
        for file_name in exclude_files:
            file_path = os.path.join(distributionDirPath(), appName() + '.app', 'Contents', 'MacOS', file_name)
            for file_path in glob.glob(file_path): # for cases with '*' in the lib name
                Functions.removeFile(file_path)
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def copyMissingLibs():
    missing_files = CONFIG['ci']['pyinstaller']['missing_pyside2_files'][Functions.osName()]
    if len(missing_files) == 0:
        Functions.printNeutralMessage(f'No missing PySide2 libraries for {Functions.osName()}')
        return
    try:
        message = 'copy missing PySide2 libraries'
        pyside2_path = PySide2.__path__[0]
        shiboken2_path = shiboken2.__path__[0]
        for file_name in missing_files:
            file_path = os.path.join(shiboken2_path, file_name)
            for file_path in glob.glob(file_path): # for cases with '*' in the lib name
                Functions.copyFile(file_path, pyside2_path)
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def copyMissingPlugins():
    missing_plugins = CONFIG['ci']['pyinstaller']['missing_pyside2_plugins'][Functions.osName()]
    if len(missing_plugins) == 0:
        Functions.printNeutralMessage(f'No missing PySide2 plugins for {Functions.osName()}')
        return
    try:
        message = 'copy missing PySide2 plugins'
        pyside2_path = PySide2.__path__[0]
        app_plugins_path = os.path.join(distributionDirPath(), appName(), 'PySide2', 'plugins')
        for relative_dir_path in missing_plugins:
            src_dir_name = os.path.basename(relative_dir_path)
            src_dir_path = os.path.join(pyside2_path, relative_dir_path)
            dst_dir_path = os.path.join(app_plugins_path, src_dir_name)
            Functions.copyDir(src_dir_path, dst_dir_path)
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

if __name__ == "__main__":
    copyMissingLibs()
    copyMissingPlugins()
    runPyInstaller()
    #excludeLibs()
