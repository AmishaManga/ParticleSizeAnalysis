"""
Author: Amisha Manga
Date: 18/07/2022
This is the coding solution to the Particle Size Analysis Problem

Usage:

Please ensure the correct path to the input images are provided.

$ python ParticleSizeAnalysis.py imagePath intMaxAllowableParticleSize

References: 
* https://pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/
* https://www.geeksforgeeks.org/circle-detection-using-opencv-python/
* https://docs.opencv.org/4.5.3/dd/d1a/group__imgproc__feature.html#ga47849c3be0d0406ad3ca45db65a25d2d

"""
import sys
import logging
from pathlib import Path
from Logger import clsLogger
import os
from os import listdir
from ImageProcessingMethods import clsImageProcessingMethods


def vMain():
    """This is the main method of the Particle Size Analysis program.

    Parameters:

    Returns:
    """

    if (len(sys.argv) != 3):
        print('Please pass two command line arguments')
        print('Example:')
        print('')
        print('$ python ParticleSizeAnalysis.py sample_particles 200')
        print('')
        return

    # Choose a name for log file
    acLogFileName = 'Logging.log'

    # Enabled logging to console, set to  True for Debugging
    bLogToConsole = True

    # Start and configure the Logger
    objClsLogger = clsLogger()
    objClsLogger.vConfigureLogger(acLogFileName, bLogToConsole)

    objPathImageDir = Path(sys.argv[1])
    intMaxAllowableParticleSizePix = sys.argv[2]

    # Verify that the path exists
    if (objPathImageDir.exists() is False):
        logging.error('Image directory %s does not exist', sys.argv[1])
        return

    # Verify that the maximum particle allowable size is provided
    if (not intMaxAllowableParticleSizePix):
        logging.error('Maximum Particle Size not provided')
        return
    
    # Verify that the image directory is not empty
    if os.listdir(objPathImageDir) == []:
        logging.error("No images found in %s directory", sys.argv[1])

    for images in os.listdir(objPathImageDir):
        # Assumption: Image type is png. and size 800 by 600.
        # Therefore Check that images are png's 
        if (images.endswith(".png")):
            strImagePath = str(objPathImageDir) + "/" + str(images)
            imageObject = clsImageProcessingMethods.ReadAndPrepImage(strImagePath)
        else:
            logging.error('No .png images found in objPathImageDir')

if __name__ == "__main__":
    vMain()
