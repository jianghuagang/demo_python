#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 储液罐开始转移信号
__author__ = 'phoenix'

import TagSimulator
import time
import random
import sys
import msvcrt

tag_access = TagSimulator.TagAccess()

# 定义 tagname
tag_thin_trans_ev 		= 'MESPY3_DI_0037'

time_interval			= 1
total_seconds			= 60


# 生成数据，
def sleep():
  time.sleep(1)


# 开始 transfer 事件
tag_access.set_tag_value(tag_thin_trans_ev, 1)
print tag_thin_trans_ev, '=', tag_access.get_tag_value(tag_thin_trans_ev)
time.sleep(total_seconds + random.randint(1,8))


# 结束 transfer 事件
tag_access.set_tag_value(tag_thin_trans_ev, 0)
print tag_thin_trans_ev, '=', tag_access.get_tag_value(tag_thin_trans_ev)

#input('Press enter to continue . . .')

sys.exit(0)