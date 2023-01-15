
# from arcgis import gis
# from arcgis.gis.server import Server
# from arcgis.gis import GIS
# from arcgis.gis.server import catalog
# from arcgis.gis import server
# import json
# from arcgis.gis.server import ServerManager
# portal = GIS(username="shuhao_xin_LearnArcGIS", password="xin13839458893//")
# #server_base_url = "https://localhost:6443/arcgis/manager"
# server_base_url = "https://localhost:6443/arcgis/"
# gis_server=Server(server_base_url, portal,username='zoney-178',password='xin13839458893//')
# detory=gis.server.catalog.ServicesDirectory(server_base_url,username='zoney-178',password='xin13839458893//')
# print(detory.url)
# print(detory.list())
# print(1)
# # manager=ServerManager(server_base_url)
#
# print('success')
# gis_server.publish_sd('test',folder='webgis')
import os
import arcgis
# from arcgis import gis
# from arcgis.gis import server
# import arcgis.gis.server.catalog
# portal = gis.GIS(username="shuhao_xin_LearnArcGIS", password="xin13839458893//")

# my_content = portal.content.search(query="owner:" + portal.users.me.username, max_items=15)
#
# gz1=my_content[8]
# print(0)


# #hostser=server.catalog.ServicesDirectory('http://abi.arcgisonline.cn/server/rest/services',portal)
# server_base_url = "https://localhost:6443/arcgis/manager"
# hostser=server.catalog.ServicesDirectory(server_base_url,username='zoney-178',password='xin13839458893//')
# sd=os.path.join(r'C:\Users\28033\Desktop','test01.sd')
# # job1=hostser.publish_sd(sd,folder='webgis')
# # job1=hostser.(sd,folder='webgis')
# gis_server=server.Server(server_base_url, portal,username='zoney-178',password='xin13839458893//')
# gis_server.site
# content=portal.content.search(query="owner:" + portal.users.me.username, max_items=15)
# content=content[3]
# content.update(shared_with={'everyone':True,'org':False,'groups':[]})
# share=content.shared_with

# #portal = gis.GIS(server_base_url,username='zoney-178',password='xin13839458893//',verify_cert=False)
# servermanager=server.ServerManager(gis=portal)
# h1=servermanager.list()[1]
# gz_item=portal.content.add('every')
# portal
# portal.users
# print('1')
# #发布一个空的服务
# from views import file2zip
# root=r'C:\Users\28033\Desktop'
# shp=os.path.join(root,'gz','gz.shp')
# zipfile=os.path.join(root,'gz','gz.zip')
# files=[shp,shp[:-4]+'.prj',shp[:-4]+'.shx',shp[:-4]+'.sbx',shp[:-4]+'.dbf',shp[:-4]+'.cpg',shp[:-4]+'.sbn']
# file2zip(zipfile,files)
#
# shpfile = portal.content.add({}, zipfile)
# published_service = shpfile.publish()
# published_service.share(everyone='true')
# print(published_service.url)
# print(1)