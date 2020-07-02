# -*- coding:GBK -*-
import yaml
import os
import getcwd
from Common import method
from Params import read_yml


def read_data(index=None,param=None):
    '''
    :param index:
    :param param:
    :return:
    '''
    path = getcwd.get_cwd()  # 获取相对路径
    yaml_path = os.path.join(path, 'Params\Param\data.yml')  # 获取配置文件路径
    with open(yaml_path, 'rb') as y:
        cont = y.read()  # 获取login.yml所有信息
        yaml.warnings({'YAMLLoadWarning': False})
        cf = yaml.load(cont)
        y.close()
    return cf[index][param]

def read_url(index=None,param=None):
    '''
    :param index:
    :param param:
    :return:
    '''
    path = getcwd.get_cwd()  # 获取相对路径
    yaml_path = os.path.join(path, 'Params\\Param\\url.yml')  # 获取配置文件路径
    with open(yaml_path, 'rb') as y:
        cont = y.read()  # 获取login.yml所有信息
        yaml.warnings({'YAMLLoadWarning': False})
        cf = yaml.load(cont)
        y.close()
    return cf[index][param]
        # print(cf[0]['openId'])

if __name__ == '__main__':
    print(read_url(0,'url'))
    print(read_url(1, 'url'))
    print(read_data(0,'data'))
    print(read_data(1,'data'))
    print(method.get_url(read_yml.read_url(1,'url')))


