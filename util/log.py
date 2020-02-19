'''
logging日志模块封装
'''

import logging


class Log(object):

    # 创建一个logger对象
    logger = logging.getLogger()

    def __init__(self):
        #设置日志级别
        self.logger.setLevel(logging.INFO)

    #创建私有方法来处理日志重复的问题
    def __console(self,name,msg):

        #设置handler文件流
        handler=logging.FileHandler(filename='./logs/app.log',  encoding='utf-8')

        #设置handler文件流格式
        formatter=logging.Formatter('%(asctime)s  -%(levelname)s -%(name)s -%(message)s')
        handler.setFormatter(formatter)

        #将handler处理器添加到logger记录器中
        self.logger.addHandler(handler)

        if  name=='debug':
            self.logger.debug(msg)

        elif name=='info':
            self.logger.info(msg)

        elif name=='warn':
            self.logger.warnings(msg,exc_info=True)

        elif name=='error':
            self.logger.error(msg,exc_info=True)        #exc_info=True输出error详细信息

        #从logger记录器对象中移除handler处理器
        self.logger.removeHandler(handler)
        #关闭handler
        handler.close()


    def debug(self,message):
        self.__console(name='debug',msg=message)

    def info(self,message):
        self.__console(name='info',msg=message)

    def warn(self,message):
        self.__console(name='warn',msg=message)

    def error(self,message):
        self.__console(name='error',msg=message)