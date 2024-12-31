from libs import *

def reflexion_simple(image):
    """
    Reflect the image about the x-axis.
    """
    H, W, C = image.shape

    cv2.imshow("Original Image", image)
    # Create a new image with the same dimensions
    refImage = np.zeros((H, W, C), dtype=np.uint8)

    # Loop over the original image
    for v in range(H):
        for u in range(W):
            # Compute the reflected coordinates
            new_v = H - 1 - v

            # Copy the pixel value
            refImage[new_v, u, :] = image[v, u, :]

    return refImage