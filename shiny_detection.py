import cv2
import numpy as np

def is_roi_mostly_white(roi_crop, brightness_threshold=240, white_percentage=0.9):
    """
    roi_crop: the cropped ROI region (BGR image from cv2)
    brightness_threshold: how close to 255 a pixel needs to be to count as "white" (0-255)
    white_percentage: what fraction of the ROI needs to be white to trigger True
    """
    gray = cv2.cvtColor(roi_crop, cv2.COLOR_BGR2GRAY)
    white_pixels = np.sum(gray >= brightness_threshold)
    total_pixels = gray.size
    ratio = white_pixels / total_pixels
    return ratio >= white_percentage, ratio