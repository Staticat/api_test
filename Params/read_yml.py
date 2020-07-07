# -*- coding:GBK -*-
import yaml
import os
import getcwd
from Config import read_config

def read_data(index=None):
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
    return cf[index]['data']


def read_url(index=None):
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

    test_url = read_config.read_config("基础信息", 'url')
    url = '/'.join([test_url,cf[index]['url']])
    return url
        # return '/'.join([test_url,url])
    # return cf[index][param]
        # print(cf[0]['openId'])

if __name__ == '__main__':
    print(read_url(0))
    print(read_url(1))
    print(read_data(0))
    print(read_data(2))



