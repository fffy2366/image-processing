#!bin/evn python
# -*- coding: utf-8 -*-
"""

auth:   jaypei
email:  jaypei97159@gmail.com

例程：
from somelib import logger

# 默认log存放目录,需要在程序入口调用才能生效,可省略
logger.log_dir = "./app"
# log文件名前缀,需要在程序入口调用才能生效,可省略
logger.log_name = "test_log"

conf = logger.Logger()
conf.debug('debug')
conf.warn('tr-warn')
conf.info('ds-info')
conf.error('ss-error')

"""

import os, time, threading
import datetime
import logging
import logging.handlers
try:
    import codecs
except ImportError:
    codecs = None

log_dir = "log"
log_name = "applog"

_logger_init_lock = threading.Lock()

class MyHandler(logging.handlers.TimedRotatingFileHandler):
    """
    自己定义的TimedRotatingFileHandler
    """
    def __init__(self, log_dir, file_name_prefix):
        self.log_dir = log_dir
        self.file_name_prefix = file_name_prefix

        self._mkdirs()

        self.baseFilename = "%s.%s.log" % (os.path.join(self.log_dir, file_name_prefix),
                time.strftime("%Y%m%d"))

        logging.handlers.TimedRotatingFileHandler.__init__(self,
                self.baseFilename,
                when='midnight', interval=1,
                backupCount=0, encoding=None)

    def doRollover(self):
        self.stream.close()
        # get the time that this sequence started at and make it a TimeTuple
        t = self.rolloverAt - self.interval
        timeTuple = time.localtime(t)
        self.baseFilename = "%s.%s.log" % (os.path.join(self.log_dir, self.file_name_prefix),
                time.strftime("%Y%m%d"))
        if self.encoding:
            self.stream = codecs.open(self.baseFilename, 'a', self.encoding)
        else:
            self.stream = open(self.baseFilename, 'a')
        self.rolloverAt = self.rolloverAt + self.interval

    def _mkdirs(self):
        if not os.path.exists(self.log_dir):
            try:
                os.makedirs(self.log_dir)
            except Exception,e:
                print str(e)

class Logger(object):
    __instance = None

    def __new__(classtype, *args, **kwargs):
        _logger_init_lock.acquire()
        if classtype != type(classtype.__instance):
            classtype.__instance = object.__new__(classtype, *args, **kwargs)
            classtype.__instance.init()

        _logger_init_lock.release()
        return classtype.__instance

    def init(self):
        # 创建日志目录
        global log_dir, log_name
        self.log_dir = log_dir
        self.log_name = log_name

        self.is_debug = True
        self.is_info = True
        self.is_warn = True
        self.is_error = True

        self.logger_formatter = "[%(asctime)-15s,%(levelname)s] %(message)s"
        self.file_formatter = "[%(asctime)-15s,%(levelname)s] %(message)s"
        self._initLogger()

    def _initLogger(self):
        # 初始化logger
        logging.basicConfig(format=self.logger_formatter)
        self.logger = logging.getLogger("_sys")
        self.logger.setLevel(logging.DEBUG)

        # info、warn、error都放到info文件
        # error单独放到error文件
        for t in (("info", logging.INFO),
                ("error", logging.ERROR)):

            filehandler = MyHandler(self.log_dir,
                    "%s.%s" % (self.log_name, t[0]))
            filehandler.suffix = "%Y%m%d.log"
            filehandler.setLevel(t[1])
            filehandler.setFormatter(logging.Formatter(self.file_formatter))
            self.logger.addHandler(filehandler)

        # debug 单独放到debug文件
        filehandler = MyHandler(self.log_dir,
                "%s.debug" % self.log_name)
        filehandler.suffix = "%Y%m%d.log"
        filehandler.setLevel(logging.DEBUG)
        filehandler.setFormatter(logging.Formatter(self.file_formatter))
        self.logger.addHandler(filehandler)

    def getLogger(self):
        return self.logger

    def debug(self, msg):
        if self.is_debug:
            self.logger.debug(msg)

    def info(self, msg):
        if self.is_info:
            self.logger.info(msg)

    def warn(self, msg):
        if self.is_warn:
            self.logger.warn(msg)

    def error(self, msg):
        if self.is_error:
            self.logger.error(msg)

def info(msg):
    Logger().info(msg)

def warn(msg):
    Logger().warn(msg)

def debug(msg):
    Logger().debug(msg)

def error(msg):
    Logger().error(msg)