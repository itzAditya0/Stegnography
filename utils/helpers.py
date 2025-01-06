import numpy as np
import cv2
from PIL import Image
from loguru import logger
from typing import Tuple, Union, Optional

def load_image(image_path: str) -> np.ndarray:
    """
    Load an image from the specified path.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        np.ndarray: Loaded image as a numpy array
    """
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Could not load image from {image_path}")
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except Exception as e:
        logger.error(f"Error loading image: {str(e)}")
        raise

def save_image(image: np.ndarray, output_path: str) -> None:
    """
    Save an image to the specified path.
    
    Args:
        image (np.ndarray): Image to save
        output_path (str): Path where to save the image
    """
    try:
        cv2.imwrite(output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        logger.info(f"Image saved successfully to {output_path}")
    except Exception as e:
        logger.error(f"Error saving image: {str(e)}")
        raise

def text_to_bits(text: str) -> str:
    """
    Convert text to binary string.
    
    Args:
        text (str): Text to convert
        
    Returns:
        str: Binary representation of text
    """
    return ''.join(format(ord(char), '08b') for char in text)

def bits_to_text(bits: str) -> str:
    """
    Convert binary string back to text.
    
    Args:
        bits (str): Binary string to convert
        
    Returns:
        str: Decoded text
    """
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

def validate_image_dimensions(image: np.ndarray, message: str) -> bool:
    """
    Validate if the image has sufficient capacity to store the message.
    
    Args:
        image (np.ndarray): Image to check
        message (str): Message to encode
        
    Returns:
        bool: True if image has sufficient capacity, False otherwise
    """
    required_pixels = len(message) * 8
    available_pixels = image.shape[0] * image.shape[1]
    return required_pixels <= available_pixels

def get_image_info(image_path: str) -> Tuple[Tuple[int, int], str]:
    """
    Get image dimensions and format.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        Tuple[Tuple[int, int], str]: ((width, height), format)
    """
    try:
        with Image.open(image_path) as img:
            return img.size, img.format.lower()
    except Exception as e:
        logger.error(f"Error getting image info: {str(e)}")
        raise
