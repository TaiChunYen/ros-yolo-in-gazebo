import cv2
import numpy as np
img = cv2.imread('./output5.jpg', 0)

height, width = img.shape[:2]
(_, thresh) = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY) 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1)) # 形态学处理:定义矩形结构
closed = cv2.erode(thresh, kernel, iterations = 1)           # 闭运算：迭代1次
#print(closed.shape)

height, width = closed.shape[:2]
v = [0]*width
z = [0]*height
a = 0

#垂直投影：统计并存储每一列的黑点数
for x in range(0, width):               
    for y in range(0, height):
        if closed[y,x] == 255:
            a = a + 1
        else :
            continue
    v[x] = a
    a = 0
    
#创建空白图片，绘制垂直投影图
roiList = []
startIndex = 0
endIndex = 0
inBlock = False


l = len(v)
emptyImage = np.zeros((height, width, 3), np.uint8) 
for x in range(0,width):
    if v[x] != height and inBlock==False:
        inBlock = True
        startIndex = x
    elif v[x] == height and inBlock==True:
        inBlock = False
        endIndex = x
        crop_img = img[:,startIndex:endIndex]
        cv2.imshow('crop_img%d'%len(roiList), crop_img)
        roiList.append(crop_img)
        
    for y in range(0, v[x]):       
        b = (255,255,255)
        emptyImage[y,x] = b





cv2.imshow('original_img',img)
cv2.imshow('erode',closed)
cv2.imshow('chuizhi', emptyImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

