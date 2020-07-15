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

def packageName():
    return f'{appName()}App'

def separator():
    return CONFIG['ci']['pyinstaller']['separator'][Functions.osName()]

def distributionDir():
    return CONFIG['ci']['project']['subdirs']['distribution']

def excludedModules():
    module_names = CONFIG['ci']['pyinstaller']['auto_exclude']
    formatted = []
    for module_name in module_names:
        formatted.append('--exclude-module')
        formatted.append(module_name)
    return formatted

def addedData():
    data = [{'from': packageName(), 'to': packageName()},
            {'from': easyTemplateLib.__path__[0], 'to': 'easyTemplateLib'},
            {'from': easyAppLogic.__path__[0], 'to': 'easyAppLogic'},
            {'from': easyAppGui.__path__[0], 'to': 'easyAppGui'},
            {'from': 'pyproject.py', 'to': '.'},
            {'from': 'pyproject.toml', 'to': '.'}]
    formatted = []
    for element in data:
        formatted.append(f'--add-data={element["from"]}{separator()}{element["to"]}')
    return formatted

def appIcon():
    icon_dir = os.path.join(*CONFIG['ci']['app']['icon']['dir'])
    icon_name = CONFIG['ci']['app']['icon']['file_name']
    icon_ext = CONFIG['ci']['app']['icon']['file_ext'][Functions.osName()]
    icon_path = os.path.join(packageName(), icon_dir, f'{icon_name}{icon_ext}')
    icon_path = os.path.abspath(icon_path)
    return f'--icon={icon_path}'

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
        app_plugins_path = os.path.join(distributionDir(), appName(), 'PySide2', 'plugins')
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

def runPyInstaller():
    try:
        message = 'freeze app'
        main_py_path = os.path.join(packageName(), 'main.py')
        work_dir = CONFIG['ci']['project']['subdirs']['build']
        pyInstallerMain([
            main_py_path,                       # Application main file
            f'--name={appName()}',              # Name to assign to the bundled app and spec file (default: first script’s basename)
            '--log-level', 'WARN',              # LEVEL may be one of DEBUG, INFO, WARN, ERROR, CRITICAL (default: INFO).
            '--noconfirm',                      # Replace output directory (default: SPECPATH/dist/SPECNAME) without asking for confirmation
            '--clean',                          # Clean PyInstaller cache and remove temporary files before building
            '--windowed',                       # Windows and Mac OS X: do not provide a console window for standard i/o.
            '--onedir',                         # Create a one-folder bundle containing an executable (default)
            #'--specpath', workDirPath(),       # Folder to store the generated spec file (default: current directory)
            '--distpath', distributionDir(),    # Where to put the bundled app (default: ./dist)
            '--workpath', work_dir,             # Where to put all the temporary work files, .log, .pyz and etc. (default: ./build)
            *excludedModules(),                 # Exclude modules
            *addedData(),                       # Add data
            appIcon()                           # Application icon
            ])
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def excludeFiles():
    file_names = CONFIG['ci']['pyinstaller']['manual_exclude']
    if len(file_names) == 0:
        Functions.printNeutralMessage(f'No libraries to be excluded for {Functions.osName()}')
        return
    try:
        message = 'exclude files'
        for file_name in file_names:
            dir_suffix = CONFIG['ci']['pyinstaller']['dir_suffix'][Functions.osName()]
            content_suffix = CONFIG['ci']['pyinstaller']['content_suffix'][Functions.osName()]
            freezed_app_path = os.path.join(distributionDir(), f'{appName()}{dir_suffix}', f'{content_suffix}')
            file_path = os.path.join(freezed_app_path, file_name)
            for file_path in glob.glob(file_path): # for cases with '*' in the lib name
                Functions.removeFile(file_path)
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

if __name__ == "__main__":
    copyMissingLibs()
    copyMissingPlugins()
    runPyInstaller()
    excludeFiles()
