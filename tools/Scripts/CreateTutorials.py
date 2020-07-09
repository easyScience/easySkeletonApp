#!/usr/bin/env python3

import os
import ffmpeg
import Functions


CONFIG = Functions.config()

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

if __name__ == "__main__":
    writeVideo()
