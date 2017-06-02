#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Yefeng'

import TagSimulator
import time
import random

tag_access = TagSimulator.TagAccess()

# 定义 tagname
# tag_stor_ev 		= 'STOR_EV'
tag_stor_cip_ev 	= 'STOR_CIP_EV'
tag_stor_sip_ev 	= 'MESPY3_DI_0071'
tag_stor_out_ev 	= 'STOR_OUT_EV'

tag_stor_cip_elec 	= 'MESPY3_AI_0056'

tag_stor_sip_temp  	= 'MESPY3_AI_0013'
tag_stor_sip_pres 	= 'MESPY3_AI_0019'

tag_stor_temp	 	= 'MESPY3_AI_0007'
tag_stor_weight 	= 'MESPY3_AI_0022'


tag_stor_tt03_temp 	= 'TK_STOR_TT03_TEMP'
tag_stor_tt08_temp 	= 'TK_STOR_TT08_TEMP'
tag_stor_tt11_temp 	= 'TK_STOR_TT11_TEMP'

time_interval			= 1

# 计算电导率
def cond(t):
    return round(-0.1649 * t + 10, 2)

def sleep():
    time.sleep(1)

# 开始父事件
# tag_access.set_tag_value(tag_stor_ev, 1)
# print tag_stor_ev, '=', tag_access.get_tag_value(tag_stor_ev)
# sleep()

# 开始 cip 事件
tag_access.set_tag_value(tag_stor_cip_ev, 1)
print tag_stor_cip_ev, '=', tag_access.get_tag_value(tag_stor_cip_ev)
sleep()

# 写电导率 tag
for t in range(60):
    tag_access.set_tag_value(tag_stor_cip_elec, cond(t))
    print tag_stor_cip_elec, '=', tag_access.get_tag_value(tag_stor_cip_elec)
    sleep()

# 结束 cip 事件
tag_access.set_tag_value(tag_stor_cip_ev, 0)
sleep()

# 开始 sip 事件
tag_access.set_tag_value(tag_stor_sip_ev, 1)
sleep()

random.seed(time.time())

# 写 sip tag
for t in range(60):
    tag_access.set_tag_value(tag_stor_sip_temp, random.randint(121, 127))
    print tag_stor_sip_temp, '=', tag_access.get_tag_value(tag_stor_sip_temp)

    # tag_access.set_tag_value(tag_stor_tt03_temp, random.randint(121, 127))
    # print tag_stor_tt03_temp, '=', tag_access.get_tag_value(tag_stor_tt03_temp)

    # tag_access.set_tag_value(tag_stor_tt08_temp, random.randint(121, 127))
    # print tag_stor_tt08_temp, '=', tag_access.get_tag_value(tag_stor_tt08_temp)

    # tag_access.set_tag_value(tag_stor_tt11_temp, random.randint(121, 127))
    # print tag_stor_tt11_temp, '=', tag_access.get_tag_value(tag_stor_tt11_temp)

    tag_access.set_tag_value(tag_stor_sip_pres, round(random.uniform(2.1, 2.7), 2))
    print tag_stor_sip_pres, '=', tag_access.get_tag_value(tag_stor_sip_pres)

    print '-----------------------------华丽丽的分割线-----------------------------'
    time.sleep(time_interval)

# 结束 sip 事件
tag_access.set_tag_value(tag_stor_sip_ev, 0)
sleep()

# 结束父事件
# tag_access.set_tag_value(tag_stor_ev, 0)
# sleep()

input('Press enter to continue . . .')
