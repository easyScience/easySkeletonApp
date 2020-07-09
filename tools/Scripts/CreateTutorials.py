#!/usr/bin/env python3

import os
import ffmpeg
import Functions


CONFIG = Functions.config()

def downloadDir():
    return CONFIG['ci']['project']['subdirs']['download']

def screenshotsDir():
    return CONFIG['ci']['project']['subdirs']['screenshots']

def tutorialsDir():
    return CONFIG['ci']['project']['subdirs']['tutorials']

def fps():
    return CONFIG['ci']['app']['tutorials']['fps']

def inputPattern():
    return f'{screenshotsDir()}/*.png'

def outputPath():
    return os.path.join(tutorialsDir(), 'tutorial.mp4')

def outputOptions():
    # https://trac.ffmpeg.org/wiki/Encode/H.264
    # https://slhck.info/video/2017/02/24/crf-guide.html
    # https://kkroening.github.io/ffmpeg-python/
    # https://github.com/kkroening/ffmpeg-python/issues/95
    return {
        'crf': 18,                  # Constant Rate Factor
        'preset': 'slower',
        'movflags': 'faststart',
        'pix_fmt': 'yuv420p'        # Pixel format
    }

def writeVideo():
    (
        ffmpeg
        .input(inputPattern(), pattern_type='glob', framerate=fps())
        .output(outputPath(), **outputOptions())
        .run(overwrite_output=True)
    )

def ffmpegZippedFileName():
    version = CONFIG['ci']['ffmpeg']['macos']['version']
    file_name_base = CONFIG['ci']['ffmpeg']['macos']['file_name_base']
    file_ext = CONFIG['ci']['ffmpeg']['macos']['file_ext']
    return f'{file_name_base}{version}{file_ext}'

def ffmpegUnzippedFilePath():
    exe = CONFIG['ci']['ffmpeg']['macos']['exe']
    return os.path.join(downloadDir(), exe)

def ffmpegDownloadUrl():
    base_url = CONFIG['ci']['ffmpeg']['macos']['base_url']
    return f'{base_url}/{ffmpegZippedFileName()}'

def ffmpegDownloadDest():
    return os.path.join(downloadDir(), f'{ffmpegZippedFileName()}')

def downloadFfmpeg():
    Functions.downloadFile(
        url=ffmpegDownloadUrl(),
        destination=ffmpegDownloadDest()
    )

def unzipFfmpeg():
    if os.path.exists(ffmpegUnzippedFilePath()):
        Functions.printNeutralMessage(f'File already exists {ffmpegUnzippedFilePath()}')
        return
    Functions.unzip(ffmpegDownloadDest(), downloadDir())
    Functions.addReadPermission(ffmpegUnzippedFilePath())

def addDownloadDestToPath():
    path = Functions.environmentVariable('PATH')
    download_dest = os.path.abspath(downloadDir())
    Functions.setEnvironmentVariable('PATH', f'{download_dest}:{path}')

if __name__ == "__main__":
    downloadFfmpeg()
    unzipFfmpeg()
    addDownloadDestToPath()
    writeVideo()
