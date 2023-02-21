import cv2
import numpy as np
import pandas as pd


img_path = '25.0.jpg'
#Reading the image with opencv
img = cv2.imread(img_path)

index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

# Average
# ans = np.average(img, axis = (0,1))
# print(ans)

# Using Mean pixels
# def get_mode(img):
#     unq,count = np.unique(img.reshape(-1,img.shape[-1]), axis=1, return_counts=True)
#     return unq[count.argmax()]

# mode = get_mode(img)
# print(mode)

# mid of img
height, width = img.shape[:2]
x, y = int(height / 2) ,int(width / 2)
b,g,r = img[y,x]
b = int(b)
g = int(g)
r = int(r)
print(r,g,b)
ans = getColorName(r,g,b)
print("Color of car is :",ans)
