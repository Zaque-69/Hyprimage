# Function to reduce quality of an image for less colors visible
def reduce_quality(image, quality_rate) : 
    import cv2, os
    from src.helpers import eprint

    # Reading the image in cv2 and compresing the quality
    try : 
        img = cv2.imread(image)
        compression_params = [cv2.IMWRITE_JPEG_QUALITY, quality_rate]
        cv2.imwrite(image, img, compression_params)
        
    except : 
        eprint("Error! Can't open the image!")