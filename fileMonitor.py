#!/usr/bin/env python
# coding=utf-8
# python version 3.7

import time
import sys
from watchdog.observers import Observer
from watchdog.events import *


class FileEventHandler(FileSystemEventHandler):

    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.showDir = False
        self.doWithouts = []
        pass

    def on_created(self, event):  # 文件创建
        for p in self.doWithouts:
            if p in event.src_path:
                return
        self.print_str(1, event.is_directory, event.src_path)

    def on_deleted(self, event):  # 文件删除
        for p in self.doWithouts:
            if p in event.src_path:
                return
        self.print_str(2, event.is_directory, event.src_path)

    def on_moved(self, event):  # 文件移动
        for p in self.doWithouts:
            if p in event.src_path:
                return
        self.print_str(3, event.is_directory, event.src_path)

    def on_modified(self, event):  # 文件修改
        for p in self.doWithouts:
            if p in event.src_path:
                return
        self.print_str(4, event.is_directory, event.src_path)

    def print_str(self, on_type=int, is_directory=bool, src_path=str):
        if on_type == 1:
            s1 = u'创建'
            colour = u'32m'  # 文件创建显示绿色
        if on_type == 2:
            s1 = u'删除'
            colour = u'31m'  # 文件删除显示红色
        if on_type == 3:
            s1 = u'移动'
            colour = u'36m'  # 文件移动显示青色
        if on_type == 4:
            s1 = u'修改'
            colour = u'34m'  # 文件修改显示蓝色
        f2d = u'文件'
        if is_directory:
            f2d = u'目录'
        pstr = time.strftime(u'[%H:%M:%S]:') + u"\033[0;%s%s\033[0m" % (
        colour, u"{0} {1}:{2}".format(f2d, s1, src_path))
        print(pstr)


def help():
    print(u"""
文件变化实时监控工具(代码审计/黑盒/白盒审计辅助工具)
基于项目修改 https://github.com/TheKingOfDuck/FileMonitor
Python库依赖：watchdog、time、sys
修改代码实现:
    1 修复无例外路径时监控失效
    2 新添可设置多个例外路径，以逗号','分割
    3 优化代码结构
    4 修改信息输出为中文
    5 修复python2中文乱码问题
""")


if __name__ == "__main__":
    # 输出提示
    help()
    # 获取输入,为兼容 python2 不做汉化
    if sys.version_info.major == 2:
        try:
            monitorDir = raw_input(time.strftime('[%H:%M:%S]:') + "Please enter a directory:")
            doWithout = raw_input(time.strftime('[%H:%M:%S]:') + "Unnecessary directory:")
            showDir = raw_input(time.strftime('[%H:%M:%S]:') + "Display directory changes(y or n):")
        except:
            pass
    else:
        monitorDir = input(time.strftime('[%H:%M:%S]:') + "Please enter a directory:")
        doWithout = input(time.strftime('[%H:%M:%S]:') + "Unnecessary directory:")
        showDir = input(time.strftime('[%H:%M:%S]:') + "Display directory changes(y or n):")
    # 参数格式化
    print(time.strftime('[%H:%M:%S]:') + "\033[0;31m%s\033[0m" % "FileMonitor is running...")
    event_handler = FileEventHandler()
    if showDir == 'y':
        event_handler.showDir = True
    if len(doWithout) > 1:
        event_handler.doWithouts = doWithout.split(',')

    observer = Observer()
    observer.schedule(event_handler, monitorDir, True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
