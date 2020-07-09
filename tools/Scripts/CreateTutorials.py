#!/usr/bin/env python3

import os, sys
import cv2
import numpy as np
import glob
import Functions


CONFIG = Functions.config()

def screenshotsDir():
    return CONFIG['ci']['project']['subdirs']['screenshots']

def tutorialsDir():
    return CONFIG['ci']['project']['subdirs']['tutorials']

def fps():
    return CONFIG['ci']['app']['tutorials']['fps']

def writeVideo():
    images = []
    in_fname_pattern = os.path.join(screenshotsDir(), '*.png')
    for in_fname in sorted(glob.glob(in_fname_pattern), key=os.path.getmtime): # sorted by modification time
        image = cv2.imread(in_fname)
        height, width, layers = image.shape
        size = (width, height)
        images.append(image)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # 'avc1', 'hvc1', 'mp4v', 'DIVX', H264, X264 ('avc1' - best compression, 'hvc1' - 2nd, but GitHub CI error: The hardware encoder may be busy, or not supported.)
    out_fname = os.path.join(tutorialsDir(), 'tutorial.mp4')
    out = cv2.VideoWriter(out_fname, fourcc, fps(), size)
    for image in images:
        out.write(image)
    out.release()

if __name__ == "__main__":
    writeVideo()
