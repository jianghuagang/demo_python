#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 稀配罐开始转移信号
__author__ = 'phoenix'

import TagSimulator
import time
import random
import sys
import msvcrt

tag_access = TagSimulator.TagAccess()

# 定义 tagname
tag_stor_trans_ev 		= 'IOS.MESPY3_DI_0020'

time_interval			= 1
total_seconds			= 60


# 生成数据，
def sleep():
  time.sleep(1)


# 开始 transfer 事件
tag_access.set_tag_value(tag_stor_trans_ev, 1)
print tag_stor_trans_ev, '=', tag_access.get_tag_value(tag_stor_trans_ev)
time.sleep(total_seconds + random.randint(1,8))


# 结束 transfer 事件
tag_access.set_tag_value(tag_stor_trans_ev, 0)
print tag_stor_trans_ev, '=', tag_access.get_tag_value(tag_stor_trans_ev)

#input('Press enter to continue . . .')

sys.exit(0)