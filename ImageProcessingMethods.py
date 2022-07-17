import logging
import cv2
import numpy as np

class clsImageProcessingMethods():
    """
    Contains all methods to process images for ore particles
    """

    @staticmethod
    def ReadAndPrepImage(acImagePathPar: str):
        """ Method to read and prepare image

        Params:
            acImagePathPar: (str) The image path 

        Returns: 
            tbd
        """
        objInputImage = cv2.imread(acImagePathPar)
        return objInputImage
