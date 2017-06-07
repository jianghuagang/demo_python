#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Yefeng'

import TagSimulator
import time
import random

tag_access = TagSimulator.TagAccess()

# 定义 tagname
tag_dens_out_ev 		= 'TK_DENS_OUT_EV'
tag_dens_temp	 		= 'TK_DENS_TEMP'
tag_dens_weight 		= 'TK_DENS_WEIGHT'

time_interval			= 3

# 计算电导率
def cond(t):
    return round(-0.1649 * t + 10, 2)

def sleep():
    time.sleep(1)

# 开始父事件
# tag_access.set_tag_value(tag_dens_ev, 1)
# print tag_dens_ev, '=', tag_access.get_tag_value(tag_dens_ev)
# sleep()

# 开始 WATER 事件
tag_access.set_tag_value(tag_dens_cip_ev, 1)
print tag_dens_cip_ev, '=', tag_access.get_tag_value(tag_dens_cip_ev)
sleep()

# 写电导率 tag
for t in range(60):
    tag_access.set_tag_value(tag_dens_cip_elec, cond(t))
    print tag_dens_cip_elec, '=', tag_access.get_tag_value(tag_dens_cip_elec)
    sleep()

# 结束 cip 事件
tag_access.set_tag_value(tag_dens_cip_ev, 0)
sleep()

# 开始 sip 事件
tag_access.set_tag_value(tag_dens_sip_ev, 1)
sleep()

random.seed(time.time())

# 写 sip tag
for t in range(60):
    tag_access.set_tag_value(tag_dens_sip_temp, random.randint(121, 127))
    print tag_dens_sip_temp, '=', tag_access.get_tag_value(tag_dens_sip_temp)

    #tag_access.set_tag_value(tag_dens_tt03_temp, random.randint(121, 127))
    #print tag_dens_tt03_temp, '=', tag_access.get_tag_value(tag_dens_tt03_temp)

    #tag_access.set_tag_value(tag_dens_tt08_temp, random.randint(121, 127))
    #print tag_dens_tt08_temp, '=', tag_access.get_tag_value(tag_dens_tt08_temp)

    #tag_access.set_tag_value(tag_dens_tt11_temp, random.randint(121, 127))
    #print tag_dens_tt11_temp, '=', tag_access.get_tag_value(tag_dens_tt11_temp)

    tag_access.set_tag_value(tag_dens_sip_pres, round(random.uniform(2.1, 2.7), 2))
    print tag_dens_sip_pres, '=', tag_access.get_tag_value(tag_dens_sip_pres)

    print '-----------------------------华丽丽的分割线-----------------------------'
    time.sleep(time_interval)

# 结束 sip 事件
tag_access.set_tag_value(tag_dens_sip_ev, 0)
sleep()

# 结束父事件
#tag_access.set_tag_value(tag_dens_ev, 0)
#sleep()

input('Press enter to continue . . .')
