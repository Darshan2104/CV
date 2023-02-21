## import dependencies
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import imutils
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def get_number_plate(actual_image_path):
    try:
        img = cv2.imread(actual_image_path)
        numberPlateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml') 
        plat_detector =  cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plates = plat_detector.detectMultiScale(img,scaleFactor=1.2,minNeighbors = 5, minSize=(25,25))   
        cropped_image = img[80:300, 150:350] # Slicing to crop the image

        for (x,y,w,h) in plates:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cropped_image = img[y:y+h,x:x+w]
        # cv2.imshow('crop-plates',cropped_image)
        # cv2.imshow('plates',img)
        # if cv2.waitKey(0) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        return cropped_image
    except Exception as e:
        print("Image not found!!!!")
        print("Add proper path of image")
        return None
    
def pre_processing(img):
    # img = cv2.imread(img_path,0)
    ## apply binary thresholding
    try:
        ret,th1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
        
        cv2.imshow("th1", th1)
        # Filtering
        bilateral_1 = cv2.bilateralFilter(th1, 25, 100, 100)  
        cv2.imshow("filter on  bilateral_thresh1",bilateral_1)
        return bilateral_1
    except:
        print("Check your pre_processing function something is wrong")
        return None


def OCR(img):
    try:
        plat_number = pytesseract.image_to_string(img, lang='eng')
        return plat_number
    except:
        print("Some thing is worng woth OCR check it again")
        return None

# =======================================================================================
# =======================================================================================

file_path = './efe/2.jpg'
number_plat_img = get_number_plate(file_path)
output = pre_processing(number_plat_img)
result = OCR(output)
print(f"Plat number: {result}")

# =======================================================================================
# =======================================================================================
if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()