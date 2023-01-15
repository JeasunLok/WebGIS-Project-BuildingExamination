import gdal
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
import pickle
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
lci1=im_data[3,:,:]/im_data[0,:,:] #NIR/B
im_data=np.stack([im_data[0,:,:],im_data[1,:,:],im_data[2,:,:],im_data[3,:,:],lci1]) #B G R NIR LCI
band=5

img3=im_data[:,512:1024,512:1024]
lb3=lb_data[512:1024,512:1024].flatten()

test_x=[]
for i in range(0,band):
    test_x.append(img3[i,:,:].flatten())
test_x=np.array(test_x).transpose(1,0) #n行4列
#归一化
scaler = StandardScaler()
test_x = scaler.fit_transform(test_x)

model_name = r'D:\zuoye\webgis\zuoye\simple_try\data\svm5'
with open(model_name+'.pickle', 'rb') as file:
    model = pickle.load(file)
    predict = model.predict(test_x)
    actual = lb3
    #_clf = clf.fit(test_x, test_y)
    OA = accuracy_score(actual, predict)
    precision = precision_score(actual, predict, pos_label=1,average='weighted')
    recall = recall_score(actual, predict, pos_label=1,average='weighted')
    # f1score = f1_score(actual, predict, pos_label=1,average='binary')
    print("总体精度: ", OA)
    print("准确率: ", precision)
    print("召回率: ", recall)
    predict=predict.reshape(len(img3[0]),len(img3[0][0]))
    plt.figure(figsize=(10, 20))
    plt.subplot(2, 1, 1)
    plt.imshow(lb_data[512:1024,512:1024])
    plt.subplot(2, 1, 2)
    plt.imshow(predict)

    plt.show()