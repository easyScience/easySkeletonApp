#!/usr/bin/env python3

import os, sys
import Functions


CONFIG = Functions.config()

def appName():
    return CONFIG['tool']['poetry']['name']

def setupExe():
    app_version = CONFIG['tool']['poetry']['version']
    setup_os = CONFIG['ci']['app']['setup']['os'][Functions.osName()]
    setup_arch = CONFIG['ci']['app']['setup']['arch'][Functions.osName()]
    setup_name = f'{appName()}_{setup_os}_{setup_arch}_v{app_version}'
    setup_file_ext = CONFIG['ci']['app']['setup']['file_ext'][Functions.osName()]
    setup_full_name = f'{setup_name}{setup_file_ext}'
    d = {
        'macos': f'{setup_full_name}/Contents/MacOS/{setup_name}',
        'ubuntu': setup_full_name,
        'windows': setup_full_name
    }
    return d[Functions.osName()]

def setupExePath():
    distribution_dir = CONFIG['ci']['project']['subdirs']['distribution']
    return os.path.join(distribution_dir, setupExe())

def runInstaller():
    scripts_dir = CONFIG['ci']['project']['subdirs']['scripts']
    try:
        message = f'install {appName()}'
        silent_script = os.path.join(scripts_dir, CONFIG['ci']['scripts']['silent_install'])
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
