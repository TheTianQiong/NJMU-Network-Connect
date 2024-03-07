from selenium import webdriver
import time
class Spider:
    def publicKey(url:str, browser: str, timeset: int = 3)-> dict:

        '''

        该函数会在运行时弹出一个浏览器窗口用于获取公钥
        :rtype: dict
        :param url:str
        请使用字符串形式标注校园网登录入口，便于适配其他学校
        :param browser:str
        此处请输入自己所装的浏览器，目前还未测试其他浏览器是否可行,浏览器包括Edge、Google、Firefox(暂不开发Safari和其他非主流浏览器)
        :param timeset:int
        请输入等待时间，默认为3。时间过短不易得到结果，时间过长程序不易结束。实测填0也可以得到结果。

        '''

        if browser.lower() == 'edge':
            driver = webdriver.Edge()
        elif browser.lower() == 'chrome':
            driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            driver = webdriver.Firefox()
        else:
            return {"result":False, "publicKeyExponent":"0", "publicKeyModulus":"0", "message":"未输入有效浏览器！"}
        driver.get(url)
        time.sleep(timeset)
        try:
            result1 = driver.execute_script('return publicKeyExponent.value')
            result2 = driver.execute_script('return publicKeyModulus.value')
        except:
            return {"result":False, "publicKeyExponent":"0", "publicKeyModulus":"0", "message":"当前网页不是登录界面！"}
        else:
            return {"result": True, "publicKeyExponent":result1, "publicKeyModulus": result2, "message":"无"}
