from .input import inputData
from .cloud import cloud_free
from .clip import shpClipRaster
import cv2
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal
from .predict import predict
from .transform import raster2poly

def lda(ldi,ldi_t):
    ldi_py=ldi.copy()
    ldi_py[ldi<ldi_t]=0
    return ldi_py

def write_img(filename,im_proj,im_geotrans,im_data):
    if 'int8' in im_data.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in im_data.dtype.name:
        datatype = gdal.GDT_UInt16
    else:
        datatype = gdal.GDT_Float32

    if len(im_data.shape) == 3:
        im_bands, im_height, im_width = im_data.shape
    else:
        im_bands, (im_height, im_width) = 1,im_data.shape

    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(filename, im_width, im_height, im_bands, datatype)

    dataset.SetGeoTransform(im_geotrans)
    dataset.SetProjection(im_proj)
    if im_bands == 1:
        dataset.GetRasterBand(1).WriteArray(im_data)
    else:
        for i in range(im_bands):
            dataset.GetRasterBand(i+1).WriteArray(im_data[i])

    del dataset

def calculate_cli(path):
    #数据读入
    img=inputData(path)

    #波段去云
    #1.同态滤波
    #b1=img[0]
    #b3=img[2]
    b1=cloud_free(img[0])
    b3=cloud_free(img[2])
    #2.中值滤波
    # b1= cv2.medianBlur(img[0], 7)#中值滤波部分去云
    # b3= cv2.medianBlur(img[2], 7)

    #计算cli
    #cli=b3/(b1+1e-8)
    cli=np.true_divide(b3, b1)

    return cli

def calculate_ldi_svm(before,after,result,out_shp):
    #计算CLI指数
    cli_bf=calculate_cli(before)
    cli_af=calculate_cli(after)

    #计算LDI指数
    #ldi=cli_af/(cli_bf+1e-8)
    ldi=np.true_divide(cli_af, cli_bf)
    plt.imshow(ldi,"gray")
    plt.title("LDI")
    plt.show()

    #ldi_svm综合效果
    change=change_svm(before,after)
    final_change=ldi*change

    #用户键入阈值进行开发区域提取
    # max=np.nanmax(ldi)
    # min=np.nanmin(ldi)
    max=np.nanmax(final_change)
    min=np.nanmin(final_change)
    print("LDI的最大值是"+str(max)+" 最小值是"+str(min))
    threshold=input("请输入阈值 ")
    #construct=lda(ldi,float(threshold))
    construct = lda(final_change, float(threshold))

    #将开发区保存为tif
    Image = gdal.Open(before)
    geoTrans = Image.GetGeoTransform()
    geoProj = Image.GetProjection()
    write_img(result, geoProj, geoTrans, construct)

    # 裁剪研究范围
    clip=shpClipRaster(raster_path=result,save_path="result.tif",shapefile_path="test.shp")
    plt.imshow(clip,'gray')
    plt.title("Construction Area")
    plt.show()

    #保存矢量
    raster2poly("result.tif",out_shp)

def change_svm(before,after):
    model = r'svm'
    pre1 = predict(before, model)
    pre2=predict(after,model)
    change=pre1*10+pre2
    change[change==1]=1
    change[change!=1]=0
    return change

if __name__ == "__main__":
    before = "2020_clip.tif"
    after = "2021_clip.tif"
    out = "construction.tif"
    out_shp="SHP.shp"

    calculate_ldi_svm(before, after, out, out_shp)






