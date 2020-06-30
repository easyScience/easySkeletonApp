#!/usr/bin/env python3

import os, sys
import Functions


CONFIG = Functions.config()

def distributionDir():
    return CONFIG['ci']['project']['subdirs']['distribution']

def source():
    app_name = CONFIG['tool']['poetry']['name']
    setup_name = f"{app_name}{CONFIG['ci']['app']['setup']['file_name_suffix']}"
    setup_file_ext = CONFIG['ci']['app']['setup']['file_ext'][Functions.osName()]
    setup_exe_path = os.path.join(distributionDir(), f'{setup_name}{setup_file_ext}')
    return setup_exe_path

def destination():
    project_name = CONFIG['tool']['poetry']['name']
    runner_os = Functions.environmentVariable('RUNNER_OS')
    short_github_ref = Functions.environmentVariable('SHORT_GITHUB_REF')
    setup_zip_name = f'{project_name}-{runner_os}-{short_github_ref}.zip'
    setup_zip_path = os.path.join(distributionDir(), setup_zip_name)
    return setup_zip_path

def zipDir():
    Functions.zipDir(source(), destination())

if __name__ == "__main__":
    zipDir()
