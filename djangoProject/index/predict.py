from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pickle

def predict(filename,model):
    dataset = gdal.Open(filename)  # 打开文件
    im_width = dataset.RasterXSize  # 栅格矩阵的列数
    im_height = dataset.RasterYSize  # 栅格矩阵的行数
    im_bands = dataset.RasterCount  # 波段数
    #im_geotrans = dataset.GetGeoTransform()  # 仿射矩阵，左上角像素的大地坐标和像素分辨率
    #im_proj = dataset.GetProjection()  # 地图投影信息，字符串表示
    im_data = dataset.ReadAsArray(0, 0, im_width, im_height)
    del dataset

    #landsat
    im_data = im_data[1:5, :, :]  # B G R NIR  #根据不同影像 改
    lci = im_data[3, :, :] / im_data[0, :, :]  # NIR/B 伪LCI
    im_data = np.stack([im_data[0, :, :], im_data[1, :, :], im_data[2, :, :], im_data[3, :, :], lci])  # B G R NIR LCI
    band = 5
    #拉伸成像元数×波段数
    test_x = []
    for i in range(0, band):
        test_x.append(im_data[i, :, :].flatten())
    test_x = np.array(test_x).transpose(1, 0)
    #标准化
    scaler = StandardScaler()
    test_x = scaler.fit_transform(test_x)

    with open(model + '.pickle', 'rb') as file:
        model = pickle.load(file)
        predict = model.predict(test_x)
        predict = predict.reshape(len(im_data[0]), len(im_data[0][0]))

    return predict

if __name__ == "__main__":
    filename1="D:\zuoye\webgis\zuoye\gz.tif"  #志新的landsat
    model = r'svm'
    predict1=predict(filename1,model)
    plt.figure(figsize=(10, 20))
    plt.imshow(predict1)

    plt.show()

#变化检测
# filename2=""
# predict2=predict(filename2,model)
# change=predict1*10+predict2
# change[change==1]=1
# change[change!=1]=0


