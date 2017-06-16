#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 浓配搅拌信号及相关数据
__author__ = 'phoenix'

import TagSimulator
import time
import random
import sys

tag_access = TagSimulator.TagAccess()

# 定义 tagname
tag_dens_mix_ev 			= 'IOS.MESPY3_DI_0008'
tag_dens_mix_rate			= 'IOS.MESPY3_AI_0009'

time_interval			= 1
total_seconds			= 300

qty_min					= 45
qty_max					= 50

# 生成搅拌的数据
def mix(min, max):
    random.seed(time.time())
    return round(random.uniform(min, max),2)

def sleep():
    time.sleep(1)


# 开始 mix 事件
tag_access.set_tag_value(tag_dens_mix_ev, 1)
sleep()

# 写 sip tag
for t in range(300):
    tag_access.set_tag_value(tag_dens_mix_rate, mix(qty_min, qty_max))
    print tag_dens_mix_rate, '=', tag_access.get_tag_value(tag_dens_mix_rate)
    print '-----------------------------华丽丽的分割线-----------------------------'
    time.sleep(1)

# 结束 mix 事件
tag_access.set_tag_value(tag_dens_mix_ev, 0)
sleep()


#input('Press enter to continue . . .')

sys.exit(0)
