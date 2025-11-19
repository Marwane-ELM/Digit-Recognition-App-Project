import cv2 as cv
import numpy as np

# Script python qui va traiter chaque image entrante depuis la caméra

def traitement(path_image):
    # Lecture en niveaux de gris
    img = cv.imread(path_image, cv.IMREAD_GRAYSCALE)
    
    # Flouter légèrement pour réduire le bruit
    img = cv.GaussianBlur(img, (3, 3), 0)
    
    # Binarisation (noir/blanc)
    _, th = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    
    # Trouver le bounding box du chiffre
    coords = cv.findNonZero(th)
    x, y, w, h = cv.boundingRect(coords)
    roi = th[y:y+h, x:x+w]
    
    # Redimensionner le chiffre (par ex. 20x20)
    digit = cv.resize(roi, (20, 20), interpolation=cv.INTER_AREA)
    
    # Le replacer dans une image noire 28x28, centré
    canvas = np.zeros((28, 28), dtype=np.uint8)
    x_offset = (28 - 20) // 2
    y_offset = (28 - 20) // 2
    canvas[y_offset:y_offset+20, x_offset:x_offset+20] = digit
    canvas = canvas.reshape(1, (len(canvas)*len(canvas)))

    return canvas