# ver. 0.0.1
# -*- coding: utf-8 -*-
import json
import os
class json_operations:
    def isExistJson(file_path: str="./options.json",create:bool=False, contents:dict={}) -> bool:
        '''
        判断是否首次运行，若无json文件，则认为首次运行
        :param file_path:str
        输入需要判断或新建的文件夹
        :param create:bool
        False认为只是单纯判断是否存在，True认为不存在需要新建
        :param content:dict
        若create为False，则此项无效
        :return:bool
        存在则返回True,反之则返回False
        '''
        if not create:
            if os.path.isfile(file_path):
                return True
            else:
                return False
        else:
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    json.dump(contents, f)
                    return False
            else:
                return True
    def updateJson(file_path: str="./options.json",contents:dict={}) -> dict:
        if not json_operations.isExistJson(file_path):
            return {'result': False, 'message': 10101}
        else:
            try:
                with open(file_path, 'r') as f:
                    contents_original = json.load(f)
                    contents_original.update(contents)
                with open(file_path, 'w') as f_new:
                    json.dump(contents_original, f_new)
            except:
                return {'result': False, 'message': 10102}
            else:
                return {'result': True, 'message': 10100}
    def checkJson(file_path: str="./options.json",contents:list={}) -> dict:
        if not json_operations.isExistJson(file_path):
            return {'result': False, 'message':10101}
        else:
            try:
                flag = True
                with open(file_path, 'r') as f:
                    content_original = json.load(f)
                    for content in contents:
                        if content not in content_original:
                            flag = False
            except:
                return {'result': False, 'message': 10112}
            else:
                if flag:
                    return {'result': True, 'message':10110}
                else:
                    return {'result': False, 'message':10111}
