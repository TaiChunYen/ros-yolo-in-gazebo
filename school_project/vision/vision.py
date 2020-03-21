import cv2 
import numpy as np 
from PIL import Image 
import os.path 
from skimage import io,data
import pytesseract

def stretch(img):
    '''
    图像拉伸函数
    '''
    maxi=float(img.max())
    mini=float(img.min())

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i,j]=(255/(maxi-mini)*img[i,j]-(255*mini)/(maxi-mini))

    return img

def dobinaryzation(img):
    '''
    二值化处理函数
    '''
    maxi=float(img.max())
    mini=float(img.min())

    x=maxi-((maxi-mini)/2)
    #二值化,返回阈值ret  和  二值化操作后的图像thresh
    ret,thresh=cv2.threshold(img,x,255,cv2.THRESH_BINARY)
    #返回二值化后的黑白图像
    return thresh

def find_rectangle(contour):
    '''
    寻找矩形轮廓
    '''
    y,x=[],[]

    for p in contour:
        y.append(p[0][0])
        x.append(p[0][1])

    return [min(y),min(x),max(y),max(x)]

def locate_license(img,afterimg):
    '''
    定位车牌号
    '''
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #找出最大的三个区域
    block=[]
    for c in contours:
        #找出轮廓的左上点和右下点，由此计算它的面积和长度比
        r=find_rectangle(c)
        a=(r[2]-r[0])*(r[3]-r[1])   #面积
        s=(r[2]-r[0])*(r[3]-r[1])   #长度比

        block.append([r,a,s])
    #选出面积最大的3个区域
    block=sorted(block,key=lambda b: b[1])[-5:]

    #使用颜色识别判断找出最像车牌的区域
    maxweight,maxindex=0,-1
    for i in range(len(block)):
        b=afterimg[block[i][0][1]:block[i][0][3],block[i][0][0]:block[i][0][2]]
        #BGR转HSV
        hsv=cv2.cvtColor(b,cv2.COLOR_BGR2HSV)
        #白牌的范围
        lower=np.array([0,0,0])
        upper=np.array([180, 255, 100])
        #根据阈值构建掩膜
        mask=cv2.inRange(hsv,lower,upper)
        #统计权值
        w1=0
        for m in mask:
            w1+=m/255

        w2=0
        for n in w1:
            w2+=n
        
        #print(w2)
        #选出最大权值的区域
        if w2>maxweight:
            maxindex=i
            maxweight=w2

    return block[maxindex][0]

def find_license(img):
    '''
    预处理函数
    '''
    m=400*img.shape[0]/img.shape[1]

    #压缩图像
    img=cv2.resize(img,(400,int(m)),interpolation=cv2.INTER_CUBIC)

    #BGR转换为灰度图像
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #灰度拉伸
    stretchedimg=stretch(gray_img)

    '''进行开运算，用来去除噪声'''
    r=16
    h=w=r*2+1
    kernel=np.zeros((h,w),np.uint8)
    cv2.circle(kernel,(r,r),r,1,-1)
    #开运算
    openingimg=cv2.morphologyEx(stretchedimg,cv2.MORPH_OPEN,kernel)
    #获取差分图，两幅图像做差  cv2.absdiff('图像1','图像2')
    strtimg=cv2.absdiff(stretchedimg,openingimg)

    #图像二值化
    binaryimg=dobinaryzation(strtimg)
    #cv2.imshow('binaryimg',binaryimg)
    #侵蝕雜訊
    kernel=np.ones((5,5),np.uint8)
    binaryimg = cv2.erode(binaryimg,kernel,iterations=1)
    #cv2.imshow('erode',binaryimg)
    #canny边缘检测
    canny=cv2.Canny(binaryimg,binaryimg.shape[0],binaryimg.shape[1])
    #cv2.imshow('canny',canny)

    '''消除小的区域，保留大块的区域，从而定位车牌'''
    #进行闭运算
    kernel=np.ones((15,15),np.uint8)
    closingimg=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
    #cv2.imshow('closingimg',closingimg)

    #进行开运算
    openingimg=cv2.morphologyEx(closingimg,cv2.MORPH_OPEN,kernel)
    #cv2.imshow('openingimg',openingimg)
    #再次进行开运算
    kernel=np.ones((11,5),np.uint8)
    openingimg=cv2.morphologyEx(openingimg,cv2.MORPH_OPEN,kernel)
    #cv2.imshow('openingimg2',openingimg)

    #消除小区域，定位车牌位置
    rect=locate_license(openingimg,img)

    return rect,img

def cut_license(afterimg,rect):
    '''
    图像分割函数
    '''
    #转换为宽度和高度
    rect[2]=rect[2]-rect[0]
    rect[3]=rect[3]-rect[1]
    rect_copy=tuple(rect.copy())
    rect=[0,0,0,0]
    #创建掩膜
    mask=np.zeros(afterimg.shape[:2],np.uint8)
    #创建背景模型  大小只能为13*5，行数只能为1，单通道浮点型
    bgdModel=np.zeros((1,65),np.float64)
    #创建前景模型
    fgdModel=np.zeros((1,65),np.float64)
    #分割图像
    cv2.grabCut(afterimg,mask,rect_copy,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img_show=afterimg*mask2[:,:,np.newaxis]

    return img_show

def deal_license(licenseimg):
    '''
    车牌图片二值化
    '''
    #车牌变为灰度图像
    gray_img=cv2.cvtColor(licenseimg,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray_img',gray_img)

    #均值滤波  去除噪声
    kernel=np.ones((3,3),np.float32)/9
    gray_img=cv2.filter2D(gray_img,-1,kernel)
    #cv2.imshow('filter2D',gray_img)

    #二值化处理
    ret,thresh=cv2.threshold(gray_img,150,255,cv2.THRESH_BINARY)

    return thresh


def find_end(start,arg,black,white,width,black_max,white_max):
    end=start+1
    for m in range(start+1,width-1):
        if (black[m] if arg else white[m])>(0.98*black_max if arg else 0.98*white_max):
            end=m
            break
    return end

if __name__=='__main__':
    img=cv2.imread('a2.jpg',cv2.IMREAD_COLOR)
    #预处理图像
    rect,afterimg=find_license(img)
    #cv2.imshow('My Image', afterimg)
    cv2.rectangle(afterimg,(rect[0],rect[1]),(rect[2],rect[3]),(0,255,0),2)
    #cv2.imshow('afterimg',afterimg)
    
    crop_img = afterimg[rect[1]:rect[3], rect[0]:rect[2]]
    #crop_img=deal_license(crop_img)
    #cv2.imshow('crop_img',crop_img)

    #cutimg=cut_license(img,rect)
    #cv2.imshow('cutimg',cutimg)

    #thresh=deal_license(cutimg)
    #cv2.imshow('thresh',thresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    text = pytesseract.image_to_string(crop_img, lang='eng',config="-psm 9 -c tessedit_char_whitelist=0123456789AB")
    print(text)






























