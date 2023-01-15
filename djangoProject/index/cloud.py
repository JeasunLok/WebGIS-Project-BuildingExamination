#median 利用云极高的反射率
import cv2
import numpy as np
import scipy.fftpack
from osgeo import gdal
import matplotlib.pyplot as plt
from .input import inputData

def imclearborder(imgBW, radius):

    # 读取灰度图像
    imgBWcopy = imgBW.copy()
    contours,hierarchy = cv2.findContours(imgBWcopy.copy(), cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE)

    imgRows = imgBW.shape[0]
    imgCols = imgBW.shape[1]

    contourList = []


    for idx in np.arange(len(contours)):

        cnt = contours[idx]
        for pt in cnt:
            rowCnt = pt[0][1]
            colCnt = pt[0][0]

            check1 = (rowCnt >= 0 and rowCnt < radius) or (rowCnt >= imgRows-1-radius and rowCnt < imgRows)
            check2 = (colCnt >= 0 and colCnt < radius) or (colCnt >= imgCols-1-radius and colCnt < imgCols)

            if check1 or check2:
                contourList.append(idx)
                break

    for idx in contourList:
        cv2.drawContours(imgBWcopy, contours, idx, (0,0,0), -1)

    return imgBWcopy

def bwareaopen(imgBW, areaPixels):

    imgBWcopy = imgBW.copy()
    contours,hierarchy = cv2.findContours(imgBWcopy.copy(), cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE)


    for idx in np.arange(len(contours)):
        area = cv2.contourArea(contours[idx])
        if (area >= 0 and area <= areaPixels):
            cv2.drawContours(imgBWcopy, contours, idx, (0,0,0), -1)

    return imgBWcopy

def cloud_free(img):
    rows = img.shape[0]
    cols = img.shape[1]

    rows = img.shape[0]
    cols = img.shape[1]

    # img[img==0]=np.nan

    imgLog = np.log1p(np.array(img, dtype="float") / 255)

    # 创建高斯掩膜
    M = 2 * rows + 1
    N = 2 * cols + 1
    sigma = 10
    (X, Y) = np.meshgrid(np.linspace(0, N - 1, N), np.linspace(0, M - 1, M))
    centerX = np.ceil(N / 2)
    centerY = np.ceil(M / 2)
    gaussianNumerator = (X - centerX) ** 2 + (Y - centerY) ** 2

    # 低通和高通滤波器
    Hlow = np.exp(-gaussianNumerator / (2 * sigma * sigma))
    Hhigh = 1 - Hlow

    HlowShift = scipy.fftpack.ifftshift(Hlow.copy())
    HhighShift = scipy.fftpack.ifftshift(Hhigh.copy())

    If = scipy.fftpack.fft2(imgLog.copy(), (M, N))
    Ioutlow = np.real(scipy.fftpack.ifft2(If.copy() * HlowShift, (M, N)))
    Iouthigh = np.real(scipy.fftpack.ifft2(If.copy() * HhighShift, (M, N)))

    gamma1 = 0.3
    gamma2 = 1.5
    Iout = gamma1 * Ioutlow[0:rows, 0:cols] + gamma2 * Iouthigh[0:rows, 0:cols]

    Ihmf = np.expm1(Iout)
    Ihmf = (Ihmf - np.min(Ihmf)) / (np.max(Ihmf) - np.min(Ihmf))
    Ihmf2 = np.array(255 * Ihmf, dtype="uint8")

    Ithresh = Ihmf2 < 65
    Ithresh = 255 * Ithresh.astype("uint8")

    Iclear = imclearborder(Ithresh, 5)

    Iopen = bwareaopen(Iclear, 120)

    # 显示结果

    cv2.imwrite('result1.jpg', Ihmf2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    plt.imshow(Ihmf2, 'gray')
    plt.show()

    return Ihmf2


if __name__ == "__main__":
    # img = cv2.imread('ori1.jpg', 0)
    img=inputData("2020_clip.tif")
    plt.imshow(img[0],'gray')
    plt.show()
    cloud_free(img[0])

#以下为同态滤波去云


