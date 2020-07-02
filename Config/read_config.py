import configparser
import getcwd
import os

def read_config(section,key):
    path = getcwd.get_cwd() #获取相对路径
    config_path = os.path.join(path, 'Config\Config.ini') #获取配置文件路径
    config = configparser.ConfigParser()
    config.read(config_path,encoding="utf-8-sig")

    # Config.get(section,key)
    return config.get(section,key)
# print(read_config("基础信息","appId"))

def appId():
    appId=read_config("基础信息","appId")
    return appId

def projectId():
    projectId=read_config("基础信息","projectId")
    return projectId

def userId():
    userId = read_config("基础信息", "userId")
    return userId