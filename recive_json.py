# test read and analysis json file

import json
import requests
from io import BytesIO
from PIL import Image
import uuid
import pandas as pd
from collections import defaultdict
import time

'''
函数名称：get_json_list()
函数功能：生成json格式数据文件
函数参数：无
返回值：无
'''
def get_json_list():
    
    # 添加command key ，利用key-value 键值对方式添加元素
    command = defaultdict(dict)
    command['type'] = 'detectionResult'

    # 获取当前时间
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    command['time'] = curr_time

    # 添加 param key
    param = defaultdict(dict)
    # 当前值需要传参获取
    param['algo'] = 'FACE'
    param['taskId'] = '1'
    param['cameraId'] = '1'
    param['msgLevel'] = '1'
    param['videoUrl'] = 'ip address'

    # 添加 value list  ，字典  嵌套 列表
    param['objList'] = []

    # 人脸识别    
    # 添加元素 rect key 字典  列表 嵌套 字典
    rect = defaultdict(dict)

    param['objList'].append(rect)
    # 坐标值需要从 face 检测框获取
    param['objList'][0]['rect']['x']='0.50'
    param['objList'][0]['rect']['y']='0.50'
    param['objList'][0]['rect']['width']='0.50'
    param['objList'][0]['rect']['height']='0.50'

    # 置信度需要获取
    param['objList'][0]['confidence'] = '0.9'
    param['objList'][0]['content'] = '0.9'
    param['objList'][0]['userID'] = '1'  # ----

    # 创建 元素 resultUrl 列表
    param['objList'][0]['resultUrl'] = []

    # 创建 字典 resultUrl 列表中 嵌套  多个字典
    resultUrl_list1 = defaultdict(dict)
    param['objList'][0]['resultUrl'].append(resultUrl_list1)
    resultUrl_list1['url'] = '/Users/kenan/Desktop/meter_reader'
    resultUrl_list1['urlType'] = 'local'
    resultUrl_list1['mediaType'] = 'pic'

    resultUrl_list2 = defaultdict(dict)
    param['objList'][0]['resultUrl'].append(resultUrl_list2)
    resultUrl_list2['url'] = '/Users/kenan/Desktop/meter_reader'  # 本机的文件路径
    resultUrl_list2['urlType'] = 'local'
    resultUrl_list2['mediaType'] = 'video'

    json_list = {'command':command,
                'param':param
    }

    json_str = json.dumps(json_list, indent=4)

    print (json_str)
    with open('test_data.json', 'w') as json_file:
        json_file.write(json_str)

    return json_str

'''
函数名称：read_analysis_json（）
函数功能：读取并解析json文件
函数参数：json_file_path：json文件路径
返回值：获取到的某一条信息
'''
def read_analysis_json(json_file_path):
    
    with open(json_file_path , 'r') as f:

        load_dict = json.load(f)
    
        load_dict = load_dict['param'] #拆第一层花括号
        load_dict_objList = load_dict['objList']  # 拆开某一层获取其中1条信息

        load_dict_algo = load_dict['algo']
        load_dict_taskID = load_dict['taskId']
        load_dict_cameraID = load_dict['cameraId']
        
        load_dict_objList_rect = load_dict_objList[0]['rect']
        load_dict_objList_confidence = load_dict_objList[0]['confidence']
        load_dict_objList_userID = load_dict_objList[0]['userID']

        # data_raw = pd.DataFrame(columns=load_dict.keys())
        # data_raw = data_raw.append(load_dict,ignore_index=True)

        # print (data_raw)

    return load_dict_algo,load_dict_taskID,load_dict_cameraID,load_dict_objList_rect , load_dict_objList_confidence , load_dict_objList_userID

'''
函数名称：save_img_from_url()
函数功能：从url地址中保存图片
函数参数：url_path：url地址
        save_path：保存图片路径
返回值：无
'''
def save_img_from_url(url_path,save_path):
    req=requests.get(url_path)
    
    #使用BytesIO接口
    image=Image.open(BytesIO(req.content))
    fileName=str(uuid.uuid4())+'.'+image.format.lower()
    print ('file name -->',fileName)
    
    with open(save_path + '/' +fileName,'wb') as f:
        f.write(req.content)

'''
    保存图片、视频的位置，-》 得到了需要传出的数据信息
    taskid camera id 
    
'''


if __name__ == "__main__":
    
    json_date_list = get_json_list()

    json_file = '/Users/kenan/Desktop/test_file/test_mini_pro/test_data.json'
    a ,b , c ,d,e,f = read_analysis_json(json_file)
    print ('test -- get value --> a -->' , a)
    print ('test -- get value --> b -->' , b)
    print ('test -- get value --> c -->' , c)

    img_url = 'https://img0.baidu.com/it/u=3101694723,748884042&fm=26&fmt=auto&gp=0.jpg'
    img_save_path = '/Users/kenan/Desktop/test_file/test_video'

    save_img_from_url(img_url,img_save_path)
    
    print ('done!')



    