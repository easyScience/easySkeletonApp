#!/usr/bin/env python3

import os, sys
import ftplib
import pathlib
import Functions


CONFIG = Functions.config()

def appName():
    return CONFIG['tool']['poetry']['name']

def localRepositoryDirPath():
    distribution_dir = CONFIG['ci']['project']['subdirs']['distribution']
    setup_os = CONFIG['ci']['app']['setup']['os'][Functions.osName()]
    repository_dir_suffix = CONFIG['ci']['app']['setup']['repository_dir_suffix']
    return os.path.join(distribution_dir, f'{appName()}{repository_dir_suffix}', setup_os)

def remoteRepositoriesRootDir():
    repository_dir_suffix = CONFIG['ci']['app']['setup']['repository_dir_suffix']
    return f'{appName()}{repository_dir_suffix}'

def connect(ftp, host, port):
    try:
        message = f'connect to ftp server'
        ftp.connect(host, port)
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def login(ftp, user, password):
    try:
        message = f'login to ftp server'
        ftp.login(user, password)
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def make_dir(ftp, destination):
    try:
        message = f'make directory {destination}'
        ftp.mkd(destination)
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def upload_file(ftp, source, destination):
    try:
        destination = destination.replace('\\', '/')
        message = f'upload file {source} to {destination}'
        dir_name = os.path.basename(destination)
        dir_names = ftp.nlst(os.path.dirname(destination))
        if dir_name not in dir_names:
            make_dir(ftp, destination)
        destination = f'{destination}/{os.path.basename(source)}'
        with open(source, 'rb') as fb:
            ftp.storbinary(f'STOR {destination}', fb)
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def upload_dir(ftp, source, destination):
    try:
        message = f'upload dir {source} to {destination}'
        root_dir_name = os.path.basename(source)
        for dir_path, _, file_names in os.walk(source):
            for file_name in file_names:
                source_file = os.path.join(dir_path, file_name)
                parent_path = os.path.relpath(source_file, source)
                parent_dir = os.path.dirname(parent_path)
                destination_dir = os.path.join(destination, root_dir_name, parent_dir).rstrip(os.path.sep)
                upload_file(ftp, source_file, destination_dir)
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def upload(ftp, source, destination):
    try:
        message = f'upload {source} to {destination}'
        if os.path.isfile(source):
            upload_file(ftp, source, destination)
        elif os.path.isdir(source):
            upload_dir(ftp, source, destination)
        else:
            Functions.printFailMessage(message)
            sys.exit()
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

if __name__ == "__main__":
    host = CONFIG['ci']['app']['setup']['ftp']['host']
    port = CONFIG['ci']['app']['setup']['ftp']['port']
    user = CONFIG['ci']['app']['setup']['ftp']['user']
    password = sys.argv[1]

    ftp = ftplib.FTP()
    connect(ftp, host, port)
    login(ftp, user, password)
    upload(ftp, localRepositoryDirPath(), remoteRepositoriesRootDir())
    ftp.quit()
