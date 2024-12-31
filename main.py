from libs import *
from translation import translate_simple
from resize import resize_simple
from reflexion import reflexion_simple
from rotation import rotation_simple
from negative import negative_simple
from gray_scale import gray_scale_simple

def main():

    # Carregar a imagem
    im_path = "/home/rsb6/Desktop/ComputerVision/imgs/shopping.webp"
    image = cv2.imread(im_path)

    choice = input("""
    Enter  \\
        1 to resize the image \\
        2 to translate the image \\
        3 to reflect the image \\
        4 to rotate the image \\
        5 to display the negative image \\
        6 to display the gray image \\
    """)
    
    if choice == "1":
        scale = float(input("Enter the scale factor: "))
        new_image = resize_simple(image, scale)
        cv2.imshow("Resized Image", new_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    elif choice == "2":
        trX = int(input("Enter the translation in x direction: "))
        trY = int(input("Enter the translation in y direction: "))
        trImage = translate_simple(trX, trY, image)
        cv2.imshow("Translated Image", trImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    elif choice == "3":
        refImage = reflexion_simple(image)
        cv2.imshow("Reflected Image", refImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    elif choice == "4":
        angle = float(input("Enter the angle of rotation: "))
        rotImage = rotation_simple(image, angle)
        cv2.imshow("Rotated Image", rotImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    elif choice == "5":
        negImage = negative_simple(image)
        cv2.imshow("Negative Image", negImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    elif choice == "6":
        grayImage = gray_scale_simple(image)
        cv2.imshow("Gray Image", grayImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print("Invalid choice.")
   
if __name__ == "__main__":
    main()