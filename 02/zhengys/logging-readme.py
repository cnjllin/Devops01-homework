#!/usr/bin/env python
#coding:utf8

"""
官方文档：
英文： https://docs.python.org/2/library/logging.html?highlight=logging
中文： http://python.usyiyi.cn/python_278/library/logging.html
参考： http://www.pythonclub.org/modules/logging
"""

>>> logging.basicConfig?

Definition: logging.basicConfig(**kwargs)
    filename    # 指定文件名把记录输出定向到文件中 如果不指定就会直接打印到屏幕上.
    filemode    # 指定打开文件的模式(默认模式为"a").|"w"
    format      # 指定字符串格式化.
    datefmt     # 指定日期格式,同time.strftime().
    level       # 指定日志的级别,默认为logging.WARNING.
    stream      # 与filename不能同时使用.
                # <指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，
                # 当stream和filename同时指定时，stream被忽略>

level:
    CRITICAL,FATAL  50      临界
    ERROR           40      错误
    WARNING,WARN    30      警告
    INFO            20      通知
    DEBUG           10      调试
    NOTSET          0

format:
     %(levelno)s        打印日志级别的数值
     %(levelname)s      打印日志级别名称
     %(pathname)s       打印当前执行程序的路径，其实就是sys.argv[0]
     %(filename)s       打印当前执行程序名
     %(funcName)s       打印日志的当前函数
     %(lineno)d         打印日志的当前行号
     %(asctime)s        打印日志的时间
     %(thread)d         打印线程ID
     %(threadName)s     打印线程名称
     %(process)d        打印进程ID
     %(message)s        打印日志信息

***********************************************分割线**************************************************************

练习1：
#!/usr/bin/env python
# coding:utf8

import logging

logging.basicConfig(level=logging.INFO)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('eror')
logging.critical('critical')    
    
由于定义的日志级别是INFO，而debug级别的值只有10，而INFO的是20所有不会打印出来，只打印大于INFO值的日志记录
一般我调试程序都是直接打印在屏幕的所以就没输出到文件了  

练习2：
#!/usr/bin/env python
# coding:utf8

import logging

logging.basicConfig(level=logging.INFO,             
    #datefmt="[%Y-%m-%d %H:%M:%S]", 
    format='%(threadName)s %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    filename='/var/log/app.log',
    filemode='w'
    )

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('eror')
logging.critical('critical')    


练习3：
logging模块还支持将线程名嵌入到各个日志消息中
下面写个利用logging模块调试多线程的例子：
#coding:utf-8
import threading
import time
import logging
logging.basicConfig(level = logging.DEBUG,
format ='[%(levelname)8s]\t (%(threadName)10s)\t %(message)30s')
def worker():
    #logging的日志格式必须是字符型，不接受float和int
    logging.debug('worker start：%s'%time.time())
    time.sleep(2)
    logging.debug('worker done：%s'%time.time())
           
def saihi():
    logging.debug('saihi start：%s'%time.time())
    time.sleep(2)
    worker()
    logging.debug('saihi done：%s'%time.time())
           
t = threading.Thread(target = saihi, name = 't')
x = threading.Thread(target = worker, name = 'x')
w = threading.Thread(target = worker)
t.start()
x.start()
w.start()
#####运行结果#####
[   DEBUG]   (         t)       saihi start：1374939516.13
[   DEBUG]   (         x)      worker start：1374939516.13
[   DEBUG]   (  Thread-1)      worker start：1374939516.13
[   DEBUG]   (         t)      worker start：1374939518.13
[   DEBUG]   (  Thread-1)       worker done：1374939518.13
[   DEBUG]   (         x)       worker done：1374939518.13
[   DEBUG]   (         t)       worker done：1374939520.13
[   DEBUG]   (         t)        saihi done：1374939520.13  
