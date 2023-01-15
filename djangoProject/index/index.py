from osgeo import gdal
# import gdal
import numpy as np
import cv2
import matplotlib.pyplot as plt
from cloud import cloud_free

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

#基于用户阈值输出开发强度图
def lda(lci,lci_t):
    lci_py=lci.copy()
    lci_py[lci<lci_t]=0
    return lci_py

#读入图片
#初相数据
im_data_bf, im_proj_bf, im_geotrans_bf = readTIFF("2020_clip.tif")
im_data_bf_8 = Tiff16to8bit(im_data_bf)
# plt.imshow(im_data_bf_8[0],"gray")
# plt.show()
# img_data_bf_8 = cv2.medianBlur(im_data_bf_8[0], 7)#中值滤波部分去云
# plt.imshow(img_data_bf_8,"gray")
# plt.show()

#末相数据
im_data_af, im_proj_af, im_geotrans_af = readTIFF("2021_clip.tif")
im_data_af_8 = Tiff16to8bit(im_data_af)

#去云
b1_bf=cloud_free(im_data_bf_8[0])
b3_bf=cloud_free(im_data_bf_8[2])
b1_af=cloud_free(im_data_af_8[0])
b3_af=cloud_free(im_data_bf_8[2])

#construction land index
cli1=np.true_divide(b3_bf,b1_bf+1e-8)
cli2=np.true_divide(b3_af,b1_af+1e-8)

#land development index
ldi=np.true_divide(cli2,cli1+1e-8)

#阈值提取函数
ldi_max = np.nanmax(ldi)
ldi_min = np.nanmin(ldi)

ldi_t=0.7#设置阈值
ldarea=lda(ldi, ldi_t)
ldarea_max=np.nanmax(ldarea)
ldarea_min=np.nanmin(ldarea)

plt.imshow(ldarea,'gray')
plt.show()
