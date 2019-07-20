#coding : SHIFT_JIS

#start module import
import cv2
import math
import numpy as np 
#end module import 

def rot(theta,img_src):
    return np.float32([[math.cos(theta),-math.sin(theta),0],
                [math.sin(theta),math.cos(theta),img_src.shape[0]*0.5]])

def func1(img_src):
    size=tuple(np.array([img_src.shape[1],img_src.shape[0]]))
    afn_mat=rot(-math.pi/4,img_src)
    img_dst=cv2.warpAffine(img_src,afn_mat,size,flags=cv2.INTER_LINEAR)
    return img_dst

def func(img_src):
    center=tuple(np.array([img_src.shape[1]*0.5,img_src.shape[0]*0.5]))
    angle=45.0
    scale=1.0
    size=tuple(np.array([img_src.shape[1],img_src.shape[0]]))
    rot_mat=cv2.getRotationMatrix2D(center,angle,scale)
    img_dst=cv2.warpAffine(img_src,rot_mat,size,flags=cv2.INTER_LINEAR)
    return img_dst

def main():
    file_src='src.png'
    file_dst='dist.png'

    img_src=cv2.imread(file_src,1)
    cv2.namedWindow('src')
    cv2.namedWindow('dst')

    #write core algorithm
    img_dst=func1(img_src)

    cv2.imshow('src',img_src)
    cv2.imshow('dst',img_dst)
    cv2.imwrite(file_dst,img_dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()