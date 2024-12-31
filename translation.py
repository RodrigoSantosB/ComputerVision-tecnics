from libs import *

def translate_simple(trX, trY, image):
    """
    Translate the image by trX pixels in the x direction and trY pixels in the y direction.
    """
    H, W, C = image.shape

    # Ensure translation offsets are within bounds
    assert abs(trX) < W and abs(trY) < H, "Translation offsets exceed image dimensions."

    # Create a new image with the same dimensions
    trImage = np.zeros((H, W, C), dtype=np.uint8)

    # Loop over the original image
    for v in range(H):
        for u in range(W):
            # Compute the translated coordinates
            new_u = u + trX
            new_v = v + trY

            # Check if the new coordinates are within bounds
            if 0 <= new_u < W and 0 <= new_v < H:
                trImage[new_v, new_u, :] = image[v, u, :]

    return trImage

