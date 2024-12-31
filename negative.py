from libs import *

def negative_simple(image):
    """
    Compute the negative of the image.
    """
    H, W, C = image.shape

    # Create a new image with the same dimensions
    negImage = np.zeros((H, W, C), dtype=np.uint8)

    cv2.imshow("Original Image", image)
    
    # Loop over the original image
    for v in range(H):
        for u in range(W):
            # Compute the negative pixel value
            negImage[v, u, :] = 255 - image[v, u, :]

    return negImage