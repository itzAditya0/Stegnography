import numpy as np
import cv2
from PIL import Image
from typing import Tuple, Union, Optional
from loguru import logger

def resize_image(image: np.ndarray, target_size: Tuple[int, int], 
                interpolation: int = cv2.INTER_LINEAR) -> np.ndarray:
    """
    Resize an image to target dimensions.
    
    Args:
        image (np.ndarray): Input image to resize
        target_size (Tuple[int, int]): Desired (width, height)
        interpolation (int): OpenCV interpolation method
        
    Returns:
        np.ndarray: Resized image
    """
    try:
        return cv2.resize(image, target_size, interpolation=interpolation)
    except Exception as e:
        logger.error(f"Error resizing image: {str(e)}")
        raise

def adjust_brightness_contrast(image: np.ndarray, 
                             brightness: float = 1.0,
                             contrast: float = 1.0) -> np.ndarray:
    """
    Adjust brightness and contrast of an image.
    
    Args:
        image (np.ndarray): Input image
        brightness (float): Brightness factor (>1 increases, <1 decreases)
        contrast (float): Contrast factor (>1 increases, <1 decreases)
        
    Returns:
        np.ndarray: Adjusted image
    """
    try:
        adjusted = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
        return adjusted
    except Exception as e:
        logger.error(f"Error adjusting image: {str(e)}")
        raise

def apply_gaussian_blur(image: np.ndarray, 
                       kernel_size: Tuple[int, int] = (5,5),
                       sigma: float = 0) -> np.ndarray:
    """
    Apply Gaussian blur to an image.
    
    Args:
        image (np.ndarray): Input image
        kernel_size (Tuple[int, int]): Size of Gaussian kernel
        sigma (float): Gaussian kernel standard deviation
        
    Returns:
        np.ndarray: Blurred image
    """
    try:
        return cv2.GaussianBlur(image, kernel_size, sigma)
    except Exception as e:
        logger.error(f"Error applying blur: {str(e)}")
        raise

def rotate_image(image: np.ndarray, 
                angle: float,
                center: Optional[Tuple[int, int]] = None) -> np.ndarray:
    """
    Rotate an image by a given angle.
    
    Args:
        image (np.ndarray): Input image
        angle (float): Rotation angle in degrees
        center (Optional[Tuple[int, int]]): Center of rotation
        
    Returns:
        np.ndarray: Rotated image
    """
    try:
        if center is None:
            height, width = image.shape[:2]
            center = (width // 2, height // 2)
            
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        return cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    except Exception as e:
        logger.error(f"Error rotating image: {str(e)}")
        raise
