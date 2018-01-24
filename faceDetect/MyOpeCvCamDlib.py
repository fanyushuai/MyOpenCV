#-*- coding: UTF-8 -*-
'''
Created on 2018-1-23

@author: 土肥圆
'''

import cv2
import numpy
import dlib

PREDICTOR_PATH = "../config/dlib/shape_predictor_68_face_landmarks.dat"  

#打开1号摄像头
cap = cv2.VideoCapture(0)

#读取一桢图像，前一个返回值是是否成功，后一个返回值是图像本身
success, frame = cap.read()

#设置人脸框的颜色
color = (0,255,0)

#定义分类器
face_cascade = cv2.CascadeClassifier('../config/cv2/haarcascade_frontalface_alt.xml')
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_PATH)  

while success:
    success, frame = cap.read()
    
    #获得当前桢彩色图像的大小
    size = frame.shape[:2]
    
    #定义一个与当前桢图像大小相同的的灰度图像矩阵
    image = numpy.zeros(size,dtype=numpy.float16)
    
    #将当前桢图像转换成灰度图像（这里有修改）
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #灰度图像进行直方图等距化
    cv2.equalizeHist(image, image)
    
    #如下三行是设定最小图像的大小
    divisor =8
    h, w = size
    
    #这里加了一个取整函数
    minSize = (int(w/divisor), int(h/divisor))
    
    #3.使用detector进行人脸检测 rects为返回的结果  
    faces = detector(image,1)  
  
    #4.输出人脸数，dets的元素个数即为脸的个数  
    if len(faces) >= 1:  
        print("{} faces detected".format(len(faces)))  
      
    
    for i in range(len(faces)):  
      
        #5.使用predictor进行人脸关键点识别  
        landmarks = numpy.matrix([[p.x,p.y] for p in predictor(image,faces[i]).parts()])  
        im = image.copy()  
      
        #使用enumerate 函数遍历序列中的元素以及它们的下标  
        for idx,point in enumerate(landmarks):  
            pos = (point[0,0],point[0,1])  
            #6.绘制特征点  
            cv2.circle(im,pos,3,color=(0,255,0))
            print pos
    #显示图像
    cv2.imshow("test", frame)
    key = cv2.waitKey(10)
    c = chr(key & 255)
    if c in ['q', 'Q', chr(27)]:
        break
