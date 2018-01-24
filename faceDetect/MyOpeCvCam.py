#-*- coding: UTF-8 -*-
'''
Created on 2018-1-23

@author: 土肥圆
'''

import cv2
import numpy as np

#打开1号摄像头
cap = cv2.VideoCapture(0)

#读取一桢图像，前一个返回值是是否成功，后一个返回值是图像本身
success, frame = cap.read()

#设置人脸框的颜色
color = (0,255,0)

#定义分类器
face_cascade = cv2.CascadeClassifier('../config/cv2/haarcascade_frontalface_alt.xml')


while success:
    success, frame = cap.read()
    
    #获得当前桢彩色图像的大小
    size = frame.shape[:2]
    
    #定义一个与当前桢图像大小相同的的灰度图像矩阵
    image = np.zeros(size,dtype=np.float16)
    
    #将当前桢图像转换成灰度图像（这里有修改）
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #灰度图像进行直方图等距化
    cv2.equalizeHist(image, image)
    
    #如下三行是设定最小图像的大小
    divisor =8
    h, w = size
    
    #这里加了一个取整函数
    minSize = (int(w/divisor), int(h/divisor))
    
    #人脸检测
    faces = face_cascade.detectMultiScale(
                                      image,
                                      scaleFactor=1.1,#表示在前后两次相继的扫描中，搜索窗口的比例系数。默认为1.1即每次搜索窗口依次扩大10%;
                                      minNeighbors=3,#表示构成检测目标的相邻矩形的最小个数(默认为3个)。如果组成检测目标的小矩形的个数和小于 min_neighbors - 1 都会被排除。如果min_neighbors 为 0, 则函数不做任何操作就返回所有的被检候选矩形框，这种设定值一般用在用户自定义对检测结果的组合程序上；
                                      minSize=minSize
                                      )
    
    #如果人脸数组长度大于0
    if len(faces) > 0:
        for face in faces:
                #对每一个人脸画矩形框
                x, y, w, h = face
                cv2.rectangle(frame, (x, y), (x+w, y+h), color,2)
        print '有人来了'
    #显示图像
    cv2.imshow("test", frame)
    key = cv2.waitKey(10)
    c = chr(key & 255)
    if c in ['q', 'Q', chr(27)]:
        break
