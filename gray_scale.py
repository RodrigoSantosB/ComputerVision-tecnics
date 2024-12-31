from libs import *


def gray_scale_simple(image):
    """
    Convert the image to gray scale.
    """
    H, W, C = image.shape

    # Create a new image with the same dimensions
    grayImage = np.zeros((H, W, 1), dtype=np.uint8)

    cv2.imshow("Original Image", image)

    # Loop over the original image
    for v in range(H):
        for u in range(W):
            # Compute the gray pixel value
            grayImage[v, u] = 0.299 * image[v, u, 2] + 0.587 * image[v, u, 1] + 0.114 * image[v, u, 0]

    return grayImage 