# ver. 0.0.1
from selenium import webdriver
import time

class Spider:

    def GetEncryptedPasswordEdge(url: str, password: str, timeset: int = 3, exe_path: str = "", **options) -> dict:
        '''
        该函数会在运行时弹出一个Edge浏览器用于获取加密后的密码
        :param url:str
        请使用字符串形式标注校园网登录入口，便于适配其他学校
        :param password:str
        此处请输入你想要加密的密码
        :param timeset:int
        请输入等待时间，默认为3。时间过短不易得到结果，时间过长程序不易结束。实测填0也可以得到结果。
        :rtype: dict
        最后返回的分别是：是否获取到加密结果、运行（错误）代码、加密后密码
        :param exe_path: str
        默认为空，填写Edge浏览器驱动位置
        :param options: 启动个性化设置
        '''
        try:
            if exe_path == "":
                driver = webdriver.Edge()
            else:
                driver = webdriver.Edge(executable_path=exe_path,capabilities=options)
        except:
            return {"result": False, "message": 11001, "password": ""}
        else:
            driver.get(url)
            time.sleep(timeset)
            try:
                EncryptedPassword = driver.execute_script('return encryptedPassword(\'%s\');' % password)
            except:
                return {"result": False, "message": 11002, "password": ""}
            else:
                return {"result": True, "message": 11000, "password": EncryptedPassword}
    def GetEncryptedPasswordChrome(url: str, password: str, timeset: int = 3, exe_path: str = "", **options) -> dict:
        '''
        该函数会在运行时弹出一个Chrome浏览器用于获取加密后的密码
        :param url:str
        请使用字符串形式标注校园网登录入口，便于适配其他学校
        :param password:str
        此处请输入你想要加密的密码
        :param timeset:int
        请输入等待时间，默认为3。时间过短不易得到结果，时间过长程序不易结束。实测填0也可以得到结果。
        :rtype: dict
        最后返回的分别是：是否获取到加密结果、运行（错误）代码、加密后密码
        :param exe_path: str
        默认为空，填写Chrome浏览器驱动位置
        :param options: 启动个性化设置
        '''
        try:
            if exe_path == "":
                driver = webdriver.Chrome()
            else:
                driver = webdriver.Chrome(executable_path=exe_path,capabilities=options)
        except:
            return {"result": False, "message": 12001, "password": ""}
        else:
            driver.get(url)
            time.sleep(timeset)
            try:
                EncryptedPassword = driver.execute_script('return encryptedPassword(\'%s\');' % password)
            except:
                return {"result": False, "message": 12002, "password": ""}
            else:
                return {"result": True, "message": 12000, "password": EncryptedPassword}

    def GetEncryptedPasswordFirefox(url: str, password: str, timeset: int = 3, exe_path: str = "", **options) -> dict:
        '''
        该函数会在运行时弹出一个Firefox浏览器用于获取加密后的密码
        :param url:str
        请使用字符串形式标注校园网登录入口，便于适配其他学校
        :param password:str
        此处请输入你想要加密的密码
        :param timeset:int
        请输入等待时间，默认为3。时间过短不易得到结果，时间过长程序不易结束。实测填0也可以得到结果。
        :rtype: dict
        最后返回的分别是：是否获取到加密结果、运行（错误）代码、加密后密码
        :param exe_path: str
        默认为空，填写Firefox浏览器驱动位置
        :param options: 启动个性化设置
        '''
        try:
            if exe_path == "":
                driver = webdriver.Firefox()
            else:
                driver = webdriver.Firefox(executable_path=exe_path,capabilities=options)
        except:
            return {"result": False, "message": 13001, "password": ""}
        else:
            driver.get(url)
            time.sleep(timeset)
            try:
                EncryptedPassword = driver.execute_script('return encryptedPassword(\'%s\');' % password)
            except:
                return {"result": False, "message": 13002, "password": ""}
            else:
                return {"result": True, "message": 13000, "password": EncryptedPassword}
