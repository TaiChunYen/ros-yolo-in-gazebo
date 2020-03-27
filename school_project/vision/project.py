import cv2
import numpy as np
import pytesseract

ori_img = cv2.imread('./output6.jpg')
img = cv2.cvtColor(ori_img,cv2.COLOR_BGR2GRAY)

height, width = img.shape[:2]
(_, thresh) = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY) 
kernel = np.ones((2,2), np.uint8)# 形态学处理:定义矩形结构cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)# 闭运算：迭代5次cv2.erode(thresh, kernel, iterations = 1)
#print(closed.shape)

height, width = closed.shape[:2]
v = [0]*width
z = [0]*height
a = 0

split_point = 0
#垂直投影：统计并存储每一列的黑点数
for x in range(0, width):               
    for y in range(0, height):
        if closed[y,x] == 255:
            a = a + 1
        else :
            continue
    if x>0.3*width and x<0.7*width and a>split_point:
        split_point = a
    v[x] = a
    a = 0
print('split_point=',split_point)
print('height=',height)
    
#创建空白图片，绘制垂直投影图
roiList = []
startIndex = 0
endIndex = 0
inBlock = False


l = len(v)
emptyImage = np.zeros((height, width, 3), np.uint8) 
for x in range(0,width):
    #print(v[x])
    if v[x] < split_point and inBlock==False:
        inBlock = True
        startIndex = x
    elif (v[x] >= split_point or x==width-1) and inBlock==True:
        inBlock = False
        endIndex = x
        crop_img = img[:,startIndex:endIndex]
        cv2.imshow('crop_img%d'%len(roiList), crop_img)
        roiList.append(crop_img)
        
    for y in range(0, v[x]):       
        b = (255,255,255)
        emptyImage[y,x] = b

if len(roiList)>=2:
    text1 = pytesseract.image_to_string(roiList[0], lang='eng',config="-psm 10 -c tessedit_char_whitelist=AB")
    print(text1)
    text2 = pytesseract.image_to_string(roiList[1], lang='eng',config="-psm 8 -c tessedit_char_whitelist=123456789")
    print(text2)


cv2.imshow('original_img',img)
cv2.imshow('erode',closed)
cv2.imshow('chuizhi', emptyImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

