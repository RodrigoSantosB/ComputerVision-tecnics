from libs import *

def rotation_simple(image, angle):
    """
    Rotate the image by the given angle.
    """
    H, W, C = image.shape

    # Compute the rotation matrix
    center = (H // 2, W // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    cv2.imshow("Original Image", image)
    
    # Perform the rotation
    rotImage = cv2.warpAffine(image, M, (W, H))

    return rotImage