#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Yefeng'

# Through tow medthods to set env.
# 1. import sys
#    sys.path.append('D:\\iHyperDB\\PythonSDK')
# 2. set PYTHONPATH=D:\iHyperDB\PythonSDK

import sys
import os

# python sdk 需要的库路径
sys.path.append('C:\\iHyperDB\\PythonSDK')

# python sdk 需要的环境变量
os.environ['PATH'] = 'C:\\iHyperDB\\executable;' + os.environ["PATH"]
os.environ['iHyperDB'] = 'C:\\iHyperDB'

import server
import tagmgr
import record
import time
import hyperdb


class TagAccess:
    # 初始化 iHyperDB 连接
    def __init__(self):
        self.__myserver = server.Server('192.168.100.136', 5678)
        self.__myserver.connect()
        self.__myserver.login('admin', 'admin')
        self.__mytagmgr = tagmgr.TagMgr(self.__myserver)

    # 设置 Tag 值
    def set_tag_value(self, tagname, value):
        try:
            tag = self.__mytagmgr.get_tag(tagname)
            snapshot = record.Record(int(time.time()), 0)
            snapshot.quality = 192
            snapshot.value = value
            snapshot.tagtype = tag.tagtype
            error_code = tag.save_snapshot(snapshot)

            if error_code != hyperdb.hd_sucess:
                print 'Failed to set tag value: {0}={1}'.format(tagname, value)
        except:
            print 'Failed to set tag value: {0}={1}'.format(tagname, value)

    # 获取 Tag 值
    def get_tag_value(self, tagname):
        try:
            tag = self.__mytagmgr.get_tag(tagname)
            record = tag.get_snapshot()
        except:
            print 'Failed to get the value of tag {0}'.format(tagname)

        return record.value
