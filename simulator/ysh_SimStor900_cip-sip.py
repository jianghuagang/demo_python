#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'phoenix'
# 储液罐CIP/SIP记录

import TagSimulator
import time
import random
import sys

tag_access = TagSimulator.TagAccess()

# 定义 tagname
tag_stor_cip_ev 	= 'MESPY3_DI_0059'
tag_stor_cip_elec 	= 'MESPY3_AI_0004'

tag_stor_sip_ev 	= 'MESPY3_DI_0071'
tag_stor_sip_temp  	= 'MESPY3_AI_0013'
tag_stor_sip_pres 	= 'MESPY3_AI_0022'


tag_stor_sip_drain_temp	= 'MESPY3_AI_0007'

time_interval			= 1
total_seconds_cip		= 10
total_seconds_sip		= 10


stor_cip_elec_begin		= 10
stor_cip_elec_end		= 0.85

stor_sip_temp_min		= 121
stor_sip_temp_max		= 127

# 计算电导率
def elec(min, max, tot, idx):
	return round( min + ( max - min ) / tot * idx + random.uniform(-0.5, 0.5) * 0.2 * ( max - min ) / tot, 2 )

def sleep():
    time.sleep(1)


# 开始 cip 事件
tag_access.set_tag_value(tag_stor_cip_ev, 1)
print tag_stor_cip_ev, '=', tag_access.get_tag_value(tag_stor_cip_ev)
sleep()

print '---------------------------------------stor cip begins---------------------------------------'
tag_access.set_tag_value(tag_stor_cip_elec, stor_cip_elec_begin)
sleep()

# 写电导率 tag
for idx in range(1, total_seconds_cip):
    tag_access.set_tag_value(tag_stor_cip_elec, elec(stor_cip_elec_begin, stor_cip_elec_end, total_seconds_cip, idx))
    print tag_stor_cip_elec, '=', tag_access.get_tag_value(tag_stor_cip_elec)
    sleep()

tag_access.set_tag_value(tag_stor_cip_elec, stor_cip_elec_end)
sleep()

# 结束 cip 事件
tag_access.set_tag_value(tag_stor_cip_ev, 0)
sleep()

print '---------------------------------------stor cip ends---------------------------------------'

# 开始 sip 事件
tag_access.set_tag_value(tag_stor_sip_ev, 1)
sleep()

print '---------------------------------------stor sip begins---------------------------------------'
random.seed(time.time())

# 写 sip tag
for t in range(total_seconds_sip):
	tag_access.set_tag_value(tag_stor_sip_temp, random.randint(stor_sip_temp_min, stor_sip_temp_max))
	tag_access.set_tag_value(tag_stor_sip_drain_temp, random.randint(stor_sip_temp_min, stor_sip_temp_max))
	tag_access.set_tag_value(tag_stor_sip_pres, round(random.uniform(2.1, 2.7), 2))

	print tag_stor_sip_temp, '=', tag_access.get_tag_value(tag_stor_sip_temp)
	print tag_stor_sip_drain_temp, '=', tag_access.get_tag_value(tag_stor_sip_drain_temp)
	print tag_stor_sip_pres, '=', tag_access.get_tag_value(tag_stor_sip_pres)

	sleep()
	random.seed(time.time())

# 结束 sip 事件
tag_access.set_tag_value(tag_stor_sip_ev, 0)
sleep()


sys.exit(0)
