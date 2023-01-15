from osgeo import gdal
import numpy as np
import cv2
from time import *


def readTIFF(tifpath):
    """
    Use GDAL to read data and transform them into arrays.
    :param tifpath:tif文件的路径
    :param bandnum:需要读取的波段
    :return:该波段的数据，narray格式。len(narray)是行数，len(narray[0])列数
    """
    image = gdal.Open(tifpath)  # 打开影像
    if image == None:
        print(tifpath + "该tif不能打开!")
        return
    im_width = image.RasterXSize  # 栅格矩阵的列数，经度方向，cols(好多人搞反)
    im_height = image.RasterYSize  # 栅格矩阵的行数，纬度方向，rows
    im_bands = image.RasterCount  # 波段数
    im_proj = image.GetProjection()  # 获取投影信息坐标系
    im_geotrans = image.GetGeoTransform()  # 仿射矩阵，具体参考GetGeoTransform
    print('tif数据:{}个行，{}个列，{}层波段.'.format(im_width, im_height, im_bands))
    im_data = image.ReadAsArray(0, 0,  im_width, im_height)
    del image  # 减少冗余
    return im_data,im_proj, im_geotrans

def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range

def Tiff16to8bit(img_16):
    if (np.max(img_16) - np.min(img_16) != 0):
        # img_nrm = (img_16 - np.min(img_16)) / (np.max(img_16) - np.min(img_16)) #计算灰度范围,归一化
        img_nrm = normalization(img_16)
        img_8 = np.uint8(255 * img_nrm)
    return img_8

def inputData(path):
    im_data, im_proj, im_geotrans = readTIFF(path)
    cov_data=Tiff16to8bit(im_data)
    return cov_data



if __name__ == "__main__":
    img=inputData("2020_clip.tif")
    #展示并存储
    cv2.imwrite("img_1.png",img[0])
    #cv2.namedWindow("img",0)#创建可以缩放大小的窗口
    cv2.imshow("img",img[0])

# #进行一些opencv的测试使用
# #canny边缘提取
# block_im = cv2.GaussianBlur(block_im, (3, 3), 0)
# canny = cv2.Canny(block_im, 30, 120)
# cv2.namedWindow("Canny",0)#创建可以缩放大小的窗口
# cv2.imshow('Canny', canny)
#
# #hough直线检测
# hough_img = block_im.copy()
# lines = cv2.HoughLinesP(canny,1,np.pi/180,30,minLineLength=60,maxLineGap=10)
# lines1 = lines[:,0,:]#提取为二维
# for x1,y1,x2,y2 in lines1[:]:
#     cv2.line(hough_img,(x1,y1),(x2,y2),(255,0,0),1)
# cv2.namedWindow("Hough",0)#创建可以缩放大小的窗口
# cv2.imshow("Hough", hough_img)
#
# #otsu阈值分割
# ret2, otsu = cv2.threshold(block_im, 0 , 255, cv2.THRESH_OTSU)
# cv2.namedWindow("Otsu",0)#创建可以缩放大小的窗口
# cv2.imshow("Otsu", otsu)
#
# cv2.waitKey()
