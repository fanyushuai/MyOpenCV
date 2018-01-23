#-*- coding: UTF-8 -*-
'''
Created on 2018-1-22

@author: 土肥圆
'''
#导入cv模块
import cv2

#读取图像，支持 bmp、jpg、png、tiff 等常用格式
image = cv2.imread(r"img/rockets.jpg")

print '加载图像'

#创建窗口
#cv2.namedWindow("Image")

#显示图像
#cv2.imshow("Image",image)

print '画图'


#对于人脸特征的一些描述
face_cascade = cv2.CascadeClassifier('config/haarcascade_frontalface_alt.xml')
print '加载特征'

#,minSize=(100, 100)
faces = face_cascade.detectMultiScale(
                                      image,
                                      scaleFactor=1.1,#表示在前后两次相继的扫描中，搜索窗口的比例系数。默认为1.1即每次搜索窗口依次扩大10%;
                                      minNeighbors=3#表示构成检测目标的相邻矩形的最小个数(默认为3个)。如果组成检测目标的小矩形的个数和小于 min_neighbors - 1 都会被排除。如果min_neighbors 为 0, 则函数不做任何操作就返回所有的被检候选矩形框，这种设定值一般用在用户自定义对检测结果的组合程序上；
                                      )

print "发现{0}张人脸!".format(len(faces))

#检测到人脸画圈
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    
cv2.imshow('faces Detected!',image)

#cv2.imwrite('C:/test.png', img);

#print '保存'
cv2.waitKey(0)

#释放窗口
cv2.destroyAllWindows()
