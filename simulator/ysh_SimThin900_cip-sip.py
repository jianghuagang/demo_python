#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'phoenix'
# 稀配罐CIP/SIP记录

import TagSimulator
import time
import random
import sys

tag_access = TagSimulator.TagAccess()

# 定义 tagname
tag_thin_cip_ev_begin 		= 'MESPY3_DI_0053'
tag_thin_cip_ev_end 		= 'MESPY3_DI_0004'
tag_thin_sip_ev		 		= 'MESPY3_DI_0068'
	
tag_thin_cip_elec 			= 'MESPY3_AI_0056'
tag_thin_sip_temp 			= 'MESPY3_AI_0012'
tag_thin_sip_pres 			= 'MESPY3_AI_0017'

tag_thin_sip_drain_temp_1 	= 'MESPY3_AI_0001'
tag_thin_sip_drain_temp_2 	= 'MESPY3_AI_0003'
tag_thin_sip_drain_temp_3 	= 'MESPY3_AI_0006'



time_interval			= 1
total_seconds_cip		= 10
total_seconds_sip		= 10


thin_cip_elec_begin		= 10
thin_cip_elec_end		= 0.85

thin_sip_temp_min		= 121
thin_sip_temp_max		= 127




# 计算电导率
def elec(min, max, tot, idx):
	return round( min + ( max - min ) / count * idx + random.uniform(-0.5, 0.5) * 0.2 * ( max - min ) / count, 2 )

def sleep():
    time.sleep(1)


# 开始 cip 事件
tag_access.set_tag_value(tag_thin_cip_ev_begin, 0)
sleep()
tag_access.set_tag_value(tag_thin_cip_ev_end, 0)
sleep()
tag_access.set_tag_value(tag_thin_sip_ev, 0)
sleep()


tag_access.set_tag_value(tag_thin_cip_ev_begin, 1)
print tag_thin_cip_ev_begin, '=', tag_access.get_tag_value(tag_thin_cip_ev_begin)
sleep()

tag_access.set_tag_value(tag_thin_cip_elec, thin_cip_elec_begin)
sleep()

# 写电导率 tag
for idx in range(1, total_seconds_cip):
    tag_access.set_tag_value(tag_thin_cip_elec, elec(thin_cip_elec_begin, thin_cip_elec_end, total_seconds_cip, idx))
    print tag_thin_cip_elec, '=', tag_access.get_tag_value(tag_thin_cip_elec)
    sleep()

tag_access.set_tag_value(tag_thin_cip_elec, thin_cip_elec_end)
sleep()

# 结束 cip 事件
tag_access.set_tag_value(tag_thin_cip_ev_end, 1)
sleep()

# cip信号复位
tag_access.set_tag_value(tag_thin_cip_ev_begin, 0)
sleep()
tag_access.set_tag_value(tag_thin_cip_ev_end, 0)
sleep()

# -----------------------------------------
# 开始 sip 事件
tag_access.set_tag_value(tag_thin_sip_ev, 1)
sleep()

# 写 sip tag
for t in range(total_seconds_sip):
	tag_access.set_tag_value(tag_thin_sip_temp, random.randint(thin_sip_temp_min, thin_sip_temp_max))
	tag_access.set_tag_value(tag_thin_sip_drain_temp_1, random.randint(thin_sip_temp_min, thin_sip_temp_max))
	tag_access.set_tag_value(tag_thin_sip_drain_temp_2, random.randint(thin_sip_temp_min, thin_sip_temp_max))
	tag_access.set_tag_value(tag_thin_sip_drain_temp_3, random.randint(thin_sip_temp_min, thin_sip_temp_max))
	tag_access.set_tag_value(tag_thin_sip_pres, round(random.uniform(2.1, 2.7), 2))

	print tag_thin_sip_temp, '=', tag_access.get_tag_value(tag_thin_sip_temp)
	print tag_thin_sip_drain_temp_1, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_1)
	print tag_thin_sip_drain_temp_2, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_2)
	print tag_thin_sip_drain_temp_3, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_3)
	print tag_thin_sip_pres, '=', tag_access.get_tag_value(tag_thin_sip_pres)

	sleep()
	random.seed(time.time())

# 结束 sip 事件
tag_access.set_tag_value(tag_thin_sip_ev, 0)
sleep()

# 结束父事件
# tag_access.set_tag_value(tag_thin_ev, 0)
# sleep()

sys.exit(0)
