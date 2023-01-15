# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from arcgis import gis
from django_pandas.io import read_frame
from tqdm import tqdm
import os
import zipfile
from datetime import datetime
from djangoProject.settings import BASE_DIR
import pandas as pd
import json
from index.final import calculate_ldi_svm   #SVM算法
from test1.models import datainfo
def result(request):
    # 获取POST请求
    #只用来接受post 请求
    if request.method == 'GET':
        url = {"Image_URL": "https://localhost:6443/arcgis/rest/services/map_1/Guangzhou2000/MapServer",
               "Feature_URL": "https://services3.arcgis.com/U26uBjSD32d7xvm2/arcgis/rest/services/pre_con/FeatureServer"}
        json_url = json.dumps(url)
        return JsonResponse(json_url, safe=False)

        # return render(request, 'test01.html')
    if request.method == "POST":
        # s = request.POST.get("start")
        # e = request.POST.get("end")
        body = json.loads(request.body)

        # url = {"Image_URL": "https://localhost:6443/arcgis/rest/services/map_1/Guangzhou2000/MapServer",
        #        "Feature_URL": "https://services3.arcgis.com/U26uBjSD32d7xvm2/arcgis/rest/services/pre_con/FeatureServer"}
        # json_url = json.dumps(url)
        # return JsonResponse(json_url, safe=False)

        s = body['Date_start']
        e = body['Date_end']
        if(len(s)==0 or len(e)==0):
            return HttpResponse("请正确输入日期范围！")
        else:
            print(s,",",e,".")
            start = datetime.strptime(s, "%Y-%m-%d").date()
            end = datetime.strptime(e, "%Y-%m-%d").date()

            # # 读取数据信息
            # # 文件直接读取
            # info_path = os.path.join(BASE_DIR,"Data\dataInfo.xlsx")
            # info = pd.read_excel(info_path, parse_dates=["date"])
            # # 通过数据库读取
            # # datainformation = datainfo.objects.all()
            # # info = read_frame(datainformation)
            # date = info["date"]
            # image_name = info["name"]
            # #
            # # #连接的数据库读取
            # # print(date,image_name)
            #
            # # 获得起始时间最近数据索引
            # date_start = (date - start).dt.days
            # abs_d_s = abs(date_start)
            # min_abs_d_s = min(abs_d_s)
            start = datetime.strptime(s, "%Y-%m-%d")
            end = datetime.strptime(e, "%Y-%m-%d")
            # 读取数据信息
            info_path = os.path.join(BASE_DIR, "Data\dataInfo.xlsx")
            info = pd.read_excel(info_path, parse_dates=["date"])
            date = info["date"]
            image_name = info["name"]

            # 获得起始时间最近数据索引
            date_start = (date - start).dt.days
            abs_d_s = abs(date_start)
            min_abs_d_s = min(abs_d_s)

            # 查找起始时间前后15天内是否有影像
            if(min_abs_d_s <= 15):
                approach_start = list(abs_d_s).index(min(abs_d_s))

                # 获得终止时间最近数据索引
                date_end = (date - end).dt.days
                abs_d_e = abs(date_end)
                min_abs_d_e = min(abs_d_e)
                # 查找终止时间前后15天内是否有影像
                if(min_abs_d_e <= 15):
                    approach_end = list(abs_d_e).index(min_abs_d_e)
                    print(date[approach_start],",",date[approach_end])

                    # 判断所选取的影像是否一致
                    if(date[approach_start] - date[approach_end] == 0):
                        # if(min_abs_d_s < min_abs_d_e):
                        return HttpResponse("该时间范围内无合适影像，无法获取变化情况！")

                    else:
                        # 获取对应时间图像文件名
                        start_image = image_name[approach_start]
                        print("start_image: ",start_image)
                        end_image = image_name[approach_end]
                        print("end_image: ",end_image)

                        # 获取文件路径
                        start_image_path = os.path.join(BASE_DIR,"Data\RSData",start_image)
                        end_image_path = os.path.join(BASE_DIR, "Data\RSData", end_image)

                        # 保存文件路径
                        tif = os.path.join(BASE_DIR,r"Data\result\tif", start_image.split(".")[0]+"_"+end_image)
                        shp = os.path.join(BASE_DIR, r"Data\result\shp", start_image.split(".")[0]+"_"+end_image.split(".")[0]+".shp")
                        print("tif:",tif)
                        print("shp",shp)

                        # 计算前后变化
                        # calculate_ldi_svm(start_image_path,end_image_path,tif,shp);
                        range = "计算的变化时间范围为：" + str(date[approach_start].strftime("%Y-%m-%d"))+" ~ "+ str(date[approach_end].strftime("%Y-%m-%d"))

                        # 打包文件
                        files = [shp, shp[:-4] + '.prj', shp[:-4] + '.shx', shp[:-4] + '.dbf']
                        zipfile = os.path.join(BASE_DIR, r"Data\result\shp", start_image.split(".")[0]+ "_"+ end_image.split(".")[0]+".zip")
                        file2zip(zipfile, files)

                        # 发布服务
                        portal = gis.GIS(username="shuhao_xin_LearnArcGIS", password="Xns8y!a4umEarcZ")
                        shpfile = portal.content.add({}, zipfile)  # 定义服务
                        published_service = shpfile.publish()
                        published_service.share(everyone='true')  # 公开发布

                        dir = {'url': str(published_service.url)}

                        # josn_des=json.dumps(dir)转化为json对象
                        # range = "计算的变化时间范围为：" + str(date[approach_start].strftime("%Y-%m-%d"))+" ~ "+ str(date[approach_end].strftime("%Y-%m-%d"))

                        # url = {"Image_URL": "https://localhost:6443/arcgis/rest/services/map_1/Guangzhou2000/MapServer",
                        #        "Feature_URL": "https://services3.arcgis.com/U26uBjSD32d7xvm2/arcgis/rest/services/pre_con/FeatureServer"}

                        url = {"Image_URL": "https://localhost:6443/arcgis/rest/services/map_1/Guangzhou2000/MapServer",
                               "Feature_URL": str(published_service.url)}

                        json_url = json.dumps(url)
                        return JsonResponse(json_url, safe=False)

                        # return HttpResponse(dir);

                else:
                    return HttpResponse("该时间范围内无合适影像，无法获取变化情况！")
            else:
                return HttpResponse("该时间范围内无合适影像，无法获取变化情况！")

#打包文件
def file2zip(zip_file_name: str, file_names: list):
    """ 将多个文件夹中文件压缩存储为zip

    :param zip_file_name:   /root/Document/test.zip
    :param file_names:      ['/root/user/doc/test.txt', ...]
    :return:
    """
    # 读取写入方式 ZipFile requires mode 'r', 'w', 'x', or 'a'
    # 压缩方式  ZIP_STORED： 存储； ZIP_DEFLATED： 压缩存储
    with zipfile.ZipFile(zip_file_name, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for fn in file_names:
            parent_path, name = os.path.split(fn)

            # zipfile 内置提供的将文件压缩存储在.zip文件中， arcname即zip文件中存入文件的名称
            # 给予的归档名为 arcname (默认情况下将与 filename 一致，但是不带驱动器盘符并会移除开头的路径分隔符)
            zf.write(fn, arcname=name)

            # 等价于以下两行代码
            # 切换目录， 直接将文件写入。不切换目录，则会在压缩文件中创建文件的整个路径
            # os.chdir(parent_path)
            # zf.write(name)




