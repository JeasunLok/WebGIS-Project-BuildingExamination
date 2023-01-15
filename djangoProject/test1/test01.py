import os
import json


# path=os.path.join(r'C:\Users\28033\Desktop\gz','gz-geo.json')
# with open(path, 'r') as gz:
#     gz=json.load(gz)
# print(gz)
import  httplib2 as httplib
import  urllib, json
import getpass
import sys
from debugpy._vendored.pydevd.pydev_sitecustomize.sitecustomize import raw_input
def main(argv=None):
    print("Start or Stop service")
    "Start or Stop service"
    # username,password
    userName = raw_input("Enter User Name:")
    password = getpass.getpass("Enter Password:")

    serverName = raw_input("Enter Server Name(IP):")
    serverPort = 6080  # 10.7开始默认6443，需要在管理员目录开启http

    folder = raw_input("Enter the folder name or Root for the root folder:")
    stopOrStart = raw_input("Enter whether you want to Start or Stop the services:")

    if str.upper(stopOrStart) != "START" and str.upper(stopOrStart) != "STOP":
        print
        "Invalid stop or start!"
        return

    token = getToken(userName, password, serverName, serverPort)
    if token == "":
        print
        "Could not generate a token with the username and password provided."
        return

    if str.upper(folder) == "ROOT":
        folder = ""
    else:
        folder += "/"

    folderURL = "/arcgis/admin/services" + "/" + folder  # 构造服务rest接口

    params = urllib.urlencode({'token': token, 'f': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    httpConn = httplib.HTTPConnection(serverName, serverPort)
    httpConn.request("POST", folderURL, params, headers)

    response = httpConn.getresponse()
    if (response.status != 200):
        httpConn.close()
        print
        "Could not read folder information!"
        return
    else:
        data = response.read()

        if not assertJsonSuccess(data):
            print
            "Error when reading the folder information!" + str(data)
        else:
            print
            "Processing folder information successfully. Now processing services......"

        dataobj = json.loads(data)

        httpConn.close()

        for item in dataobj['services']:
            fullservicename = item['serviceName'] + "." + item['type']
            print
            fullservicename
            stopOrStartURL = "/arcgis/admin/services/" + folder + fullservicename + "/" + stopOrStart
            print
            stopOrStartURL
            httpConn.request("POST", urllib.quote(stopOrStartURL.encode('utf-8')), params, headers)

            stopStartresponse = httpConn.getresponse()
            if (stopStartresponse.status != 200):
                httpConn.close()
                print
                "Error while excuting stop or start. Please check the url and try again!"
                return
            else:
                stopStartdata = stopStartresponse.read()

                if not assertJsonSuccess(stopStartdata):
                    if str.upper(stopOrStart) == "START":
                        print
                        "Error returned when start service" + fullservicename
                    else:
                        print
                        "Error returned when stop services" + fullservicename

                    print
                    str(stopStartdata)
                else:
                    print
                    "Service " + fullservicename + " processed successfully!"

            httpConn.close()

        return


def getToken(username, password, serverName, serverPort):
    tokenURL = "/arcgis/admin/generateToken"

    params = urllib.urlencode({'username': username, 'password': password, 'client': 'requestip', 'f': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    httpconn = httplib.HTTPConnection(serverName, serverPort)
    httpconn.request("POST", tokenURL, params, headers)

    response = httpconn.getresponse()
    if (response.status != 200):
        httpconn.close()
        print
        "Error while attempting to start the services"
        return
    else:
        data = response.read()
        httpconn.close()

        token = json.loads(data)
        return token['token']


def assertJsonSuccess(data):
    obj = json.loads(data)
    if 'status' in obj and obj['status'] == "error":
        print
        "Error: JSON object returns an error. " + str(obj)
        return False
    else:
        return True


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
