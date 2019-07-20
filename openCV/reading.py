import numpy as np 
import cv2
def main():
    img=cv2.imread("logo.png")
    print(img)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()