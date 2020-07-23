# -*- coding:GBK -*-
import yaml
import os
import getcwd
from Config import read_config

def read_headers(index=0):
    '''
    读取headers,默认读取第一个
    :param index:
    :param param:
    :return:
    '''
    path = getcwd.get_cwd()  # 获取相对路径
    yaml_path = os.path.join(path, 'Params\Param\headers.yml')  # 获取配置文件路径
    with open(yaml_path, 'rb') as y:
        cont = y.read()  # 获取data.yml所有信息
        yaml.warnings({'YAMLLoadWarning': False})
        cf = yaml.load(cont)
        y.close()
    return cf[index]['headers']

def read_data(index=None):
    '''
    :param index:
    :param param:
    :return:
    '''
    path = getcwd.get_cwd()  # 获取相对路径
    yaml_path = os.path.join(path, 'Params\Param\data.yml')  # 获取配置文件路径
    with open(yaml_path, 'rb') as y:
        cont = y.read()  # 获取data.yml所有信息
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
        cont = y.read()  # url.yml所有信息
        yaml.warnings({'YAMLLoadWarning': False})
        cf = yaml.load(cont)
        y.close()
    test_url = read_config.read_config("基础信息", 'url')
    url = '/'.join([test_url,cf[index]['url']])
    return url

def set_headers_yaml(key,value):
    """
    设置headers.yml内容
    :param key:
    :param value:
    :return:
    """
    path = getcwd.get_cwd()  # 获取相对路径
    yaml_path = os.path.join(path, 'Params\Param\headers.yml')  # 获取配置文件路径
    with open(yaml_path, 'r', encoding='utf-8') as f:
        lines = []  # 创建了一个空列表，里面没有元素
        for line in f.readlines():
            if line != '\n':
                lines.append(line)
        f.close()
    with open(yaml_path, 'w', encoding='utf-8') as f:
        for line in lines:
            str1 = "'" + key + "'"
            str2 = '"' + key + '"'
            if str1 in line or str2 in line and "#" not in line:
                num = line.find("{")
                str = line[num:]
                dict=eval(str)
                dict[key] = value
                leftstr = line.split(":")[0]
                newline = "{0}: {1}".format(leftstr, dict)
                f.write('%s\n' % newline)
                # print(newline)
            else:
                f.write('%s' % line)
        f.close()

def set_data_yaml(key,value):
    """
    设置data.yml内容
    :param key:
    :param value:
    :return:
    """
    path = getcwd.get_cwd()  # 获取相对路径
    yaml_path = os.path.join(path, 'Params\Param\data.yml')  # 获取配置文件路径
    with open(yaml_path, 'r', encoding='utf-8') as f:
        lines = []  # 创建了一个空列表，里面没有元素
        for line in f.readlines():
            if line != '\n':
                lines.append(line)
        f.close()
    with open(yaml_path, 'w', encoding='utf-8') as f:
        for line in lines:
            str1 = "'" + key + "'"
            str2 = '"' + key + '"'
            if str1 in line or str2 in line and "#" not in line: #兼容""  ''的数据
                num = line.find("{")
                str = line[num:]
                dict=eval(str)
                dict[key] = value
                leftstr = line.split(":")[0]
                newline = "{0}: {1}".format(leftstr, dict)
                f.write('%s\n' % newline)
                # print(newline)
            else:
                f.write('%s' % line)
        f.close()
if __name__ == '__main__':
    print(read_url(0))
    print(read_url(1))




