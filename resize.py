from libs import *

def resize_simple(image, scale):
    """
    Resize the image by the given scale factor.
    """
    H, W, C = image.shape
    
    print("Original shape: ", image.shape)
    
    # Compute the new image dimensions
    new_H = int(H * scale)
    new_W = int(W * scale)

    # Create a new image with the new dimensions
    new_image = np.zeros((new_H, new_W, C), dtype=np.uint8)

    #output image shape
    print("New shape: ", new_image.shape) 
    
    # Loop over the new image
    for v in range(new_H):
        for u in range(new_W):
            # Compute the coordinates in the original image
            new_u = int(u / scale)
            new_v = int(v / scale)

            # Ensure the coordinates are within bounds
            if 0 <= new_u < W and 0 <= new_v < H:
                new_image[v, u, :] = image[new_v, new_u, :]

    return new_image