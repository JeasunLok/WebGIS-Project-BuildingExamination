from osgeo import gdal
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
import pickle
# 读图像文件
def read_img(filename):
    dataset = gdal.Open(filename)  # 打开文件
    im_width = dataset.RasterXSize  # 栅格矩阵的列数
    im_height = dataset.RasterYSize  # 栅格矩阵的行数
    im_bands = dataset.RasterCount  # 波段数
    #im_geotrans = dataset.GetGeoTransform()  # 仿射矩阵，左上角像素的大地坐标和像素分辨率
    #im_proj = dataset.GetProjection()  # 地图投影信息，字符串表示
    im_data = dataset.ReadAsArray(0, 0, im_width, im_height)

    del dataset

    return im_width, im_height, im_bands,im_data

im_width, im_height, im_bands,im_data=read_img("D:\zuoye\webgis\zuoye\simple_try\data\Sentinel_image.tif")
lb_width, lb_height, lb_bands,lb_data=read_img("D:\zuoye\webgis\zuoye\simple_try\data\setinel_lb.tif")

ndvi1=(im_data[3,:,:]-im_data[2,:,:])/(im_data[3,:,:]+im_data[2,:,:])
lci1=im_data[3,:,:]/im_data[0,:,:]

im_data=np.stack([im_data[0,:,:],im_data[1,:,:],im_data[2,:,:],im_data[3,:,:],lci1])
band=5
#分幅
img1=im_data[:,0:512,:]
img2=im_data[:,512:1024,0:512]

lb1=lb_data[0:512,:]
lb2=lb_data[512:1024,0:512]


#掩膜
mask1=lb1!=0
mask2=lb2!=0
train1=mask1*img1
train2=mask2*img2


x=[]
for i in range(0,band):
    tmp=np.hstack((train1[i,:,:].flatten(), train2[i,:,:].flatten()))
    x.append(tmp)

x=np.array(x).transpose(1,0)
scaler = StandardScaler()
x = scaler.fit_transform(x)
print(x.shape)
#y=lb1[lb1!=0]

y=np.hstack((lb1.flatten(), lb2.flatten()))
print(y.shape)





def PolynomialSVC(degree, C=1.5):
    return Pipeline([
        ("poly", PolynomialFeatures(degree=degree)),
        ("std_scaler", StandardScaler()),
        ("linearSVC", LinearSVC(C=C))])

poly_svc = PolynomialSVC(degree=2)
poly_svc.fit(x, y)
model_name = r'svm'
with open('{}.pickle'.format(model_name), 'wb') as fw:
    pickle.dump(poly_svc, fw)