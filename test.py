import requests
from Common import method
import json
from Params import read_yml
url = method.get_url(read_yml.read_url(1,'url'))
json1 = read_yml.read_data(1,'data')
# json1={
#     "projectId":"537712031151685632",
#     "type":0,
#     "subTypeName":"",
#     "taskId":"715290265899762513",
#     "taskProgress":0,
#     "address":"深圳市福田区人民政府附近",
#     "nearBy":"深圳市福田区福民路214号",
#     "city":"深圳市",
#     "content":"测试发布一个自动化动态",
#     "originalContent":"测试发布一个自动化动态",
#     "country":"中国",
#     "county":"福田区",
#     "imgs":[
#         {
#             "compressImgPath":"https://xcxprd.tgct.com.cn/api/fileservice/file/dynamic/download/718186494132486158",
#             "imgPath":"https://xcxprd.tgct.com.cn/api/fileservice/file/dynamic/download/718178414225260617",
#             "compressImgId":"718186494132486158",
#             "id":"718178414225260617"
#         },
#         {
#             "compressImgPath":"https://xcxprd.tgct.com.cn/api/fileservice/file/dynamic/download/718186494132486159",
#             "imgPath":"https://xcxprd.tgct.com.cn/api/fileservice/file/dynamic/download/718178414225260618",
#             "compressImgId":"718186494132486159",
#             "id":"718178414225260618"
#         }
#     ],
#     "videos":[
#         {
#             "id":"718186494132486162"
#         }
#     ],
#     "fileIdList":[
#         "718186494132486160",
#         "718186494132486161"
#     ],
#     "latitude":22.52291,
#     "longitude":114.05454,
#     "province":"广东省",
#     "receiveUserIdList":[
#
#     ],
#     "receiveTeamIdList":[
#
#     ],
#     "accessableUserIdList":[
#         "-1"
#     ],
#     "accessableTeamIdList":[
#         "-1"
#     ],
#     "weather":"阴",
#     "temperature":"29℃",
#     "remindAddDto":None,
#     "remindId":""
# }

headers = {"Content-Type":"application/json","Accept": "*/*", "appId": "wxcd03432c1d3bfcb7","token":"943c2afe-0e22-4fa1-bde8-fe8a5812d589"}
r=method.HttpRequest()
res =r.run_method(url=url,method="POST",json=json1,headers=headers)
# res=requests.post(url=url,json=json1,headers=headers,data=None)
print(res.json())
print(res.json()["resModel"])