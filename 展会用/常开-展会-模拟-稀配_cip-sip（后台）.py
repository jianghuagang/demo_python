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
tag_thin_cip_ev_begin 		= 'IOS.MESPY3_DI_0053'
tag_thin_cip_ev_end 		= 'IOS.MESPY3_DI_0004'
tag_thin_sip_ev		 		= 'IOS.MESPY3_DI_0068'
	
tag_thin_cip_elec 			= 'IOS.MESPY3_AI_0004'
tag_thin_sip_temp 			= 'IOS.MESPY3_AI_0012'
tag_thin_sip_pres 			= 'IOS.MESPY3_AI_0017'

tag_thin_sip_drain_temp_1 	= 'IOS.MESPY3_AI_0001'
tag_thin_sip_drain_temp_2 	= 'IOS.MESPY3_AI_0003'
tag_thin_sip_drain_temp_3  	= 'IOS.MESPY3_AI_0006'



time_interval			= 1
total_seconds_cip		= 60
total_seconds_sip		= 60
total_seconds_ideal		= 30


thin_cip_elec_begin		= 9.8
thin_cip_elec_end		= 0.23

thin_sip_temp_min		= 121
thin_sip_temp_max		= 127

thin_room_temp_min		= 20
thin_room_temp_max		= 25

total_seconds_sip_normal	= 30
total_seconds_sip_heating	= 30
total_seconds_sip_cooling	= 30



# 计算电导率
def elec(min, max, tot, idx):
	return round( min + ( max - min ) / tot * idx + random.uniform(-0.5, 0.5) * 0.2 * ( max - min ) / tot, 2 )
	
# 模拟降温，模拟升温
def simu_line(val1, val2, tot, idx):
	return val1 + ( val2 - val1 ) / tot * ( idx - random.uniform(-0.5, 0.5) * 0.39 )


# 模拟常温
def simu_random(val1, val2):
	random.uniform(val1, val2)

def sleep():
    time.sleep(1)


while 1:
	# 开始 cip 事件
	tag_access.set_tag_value(tag_thin_cip_ev_begin, 0)
	sleep()
	tag_access.set_tag_value(tag_thin_cip_ev_end, 0)
	sleep()
	tag_access.set_tag_value(tag_thin_sip_ev, 0)
	sleep()
	
	print '-------------------------thin cip begins-------------------------'
	print tag_thin_cip_ev_begin, '=', tag_access.get_tag_value(tag_thin_cip_ev_begin)
	print tag_thin_cip_ev_end, '=', tag_access.get_tag_value(tag_thin_cip_ev_end)
	print '-------------------------'


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
	print '-------------------------thin cip ends-------------------------'
	print tag_thin_cip_ev_begin, '=', tag_access.get_tag_value(tag_thin_cip_ev_begin)
	print tag_thin_cip_ev_end, '=', tag_access.get_tag_value(tag_thin_cip_ev_end)
	print '-------------------------'


	print '-------------------------------sip normal-------------------------------'
	# 常温区
	for t in range(total_seconds_sip_normal):
		tag_access.set_tag_value(tag_thin_sip_temp, random.randint(thin_room_temp_min, thin_room_temp_max))
		tag_access.set_tag_value(tag_thin_sip_drain_temp_1, random.randint(thin_room_temp_min, thin_room_temp_max))
		tag_access.set_tag_value(tag_thin_sip_drain_temp_2, random.randint(thin_room_temp_min, thin_room_temp_max))
		tag_access.set_tag_value(tag_thin_sip_drain_temp_3, random.randint(thin_room_temp_min, thin_room_temp_max))
		tag_access.set_tag_value(tag_thin_sip_pres, round(random.uniform(0.5, 0.75), 2))

		print tag_thin_sip_temp, '=', tag_access.get_tag_value(tag_thin_sip_temp)
		print tag_thin_sip_drain_temp_1, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_1)
		print tag_thin_sip_drain_temp_2, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_2)
		print tag_thin_sip_drain_temp_3, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_3)
		print tag_thin_sip_pres, '=', tag_access.get_tag_value(tag_thin_sip_pres)

		sleep()
		random.seed(time.time())



	print '-------------------------------sip heating-------------------------------'
	# 升温区
	for t in range(total_seconds_sip_heating):
		tag_access.set_tag_value(tag_thin_sip_temp, round(simu_line(thin_room_temp_max + 2, thin_sip_temp_min - 2, total_seconds_sip_heating, t), 1 ) )
		tag_access.set_tag_value(tag_thin_sip_drain_temp_1, round(simu_line(thin_room_temp_max + 2, thin_sip_temp_min - 2, total_seconds_sip_heating, t), 1 ) )
		tag_access.set_tag_value(tag_thin_sip_drain_temp_2, round(simu_line(thin_room_temp_max + 2, thin_sip_temp_min - 2, total_seconds_sip_heating, t), 1 ) )
		tag_access.set_tag_value(tag_thin_sip_drain_temp_3, round(simu_line(thin_room_temp_max + 2, thin_sip_temp_min - 2, total_seconds_sip_heating, t), 1 ) )
		tag_access.set_tag_value(tag_thin_sip_pres, round(simu_line(0.75, 1.98, total_seconds_sip_heating, t), 2))

		print tag_thin_sip_temp, '=', tag_access.get_tag_value(tag_thin_sip_temp)
		print tag_thin_sip_drain_temp_1, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_1)
		print tag_thin_sip_drain_temp_2, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_2)
		print tag_thin_sip_drain_temp_3, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_3)
		print tag_thin_sip_pres, '=', tag_access.get_tag_value(tag_thin_sip_pres)

		sleep()
		random.seed(time.time())	
	
	
	# ---------------------------
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

		print '-----------------------------华丽丽的分割线-----------------------------'
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
	
	print '---------------------------------------thin sip ends---------------------------------------'
	print tag_thin_sip_ev, '=', tag_access.get_tag_value(tag_thin_sip_ev)
	print '-------------------------'
	
	
	print '-------------------------------sip cooling-------------------------------'
	# 降温区
	for t in range(total_seconds_sip_cooling):
		tag_access.set_tag_value(tag_thin_sip_temp, round(simu_line(thin_sip_temp_max - 2, thin_room_temp_max - 2, total_seconds_sip_cooling, t), 0 ) )
		tag_access.set_tag_value(tag_thin_sip_drain_temp_1, round(simu_line(thin_sip_temp_max - 2, thin_room_temp_max - 2, total_seconds_sip_cooling, t), 0 ) )
		tag_access.set_tag_value(tag_thin_sip_drain_temp_2, round(simu_line(thin_sip_temp_max - 2, thin_room_temp_max - 2, total_seconds_sip_cooling, t), 0 ) )
		tag_access.set_tag_value(tag_thin_sip_drain_temp_3, round(simu_line(thin_sip_temp_max - 2, thin_room_temp_max - 2, total_seconds_sip_cooling, t), 0 ) )
		tag_access.set_tag_value(tag_thin_sip_pres, round(simu_line(1.98, 0.75, total_seconds_sip_cooling, t), 2))

		print tag_thin_sip_temp, '=', tag_access.get_tag_value(tag_thin_sip_temp)
		print tag_thin_sip_drain_temp_1, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_1)
		print tag_thin_sip_drain_temp_2, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_2)
		print tag_thin_sip_drain_temp_3, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_3)
		print tag_thin_sip_pres, '=', tag_access.get_tag_value(tag_thin_sip_pres)

		sleep()
		random.seed(time.time())


	# ideal time 
	time.sleep(total_seconds_ideal)

# 结束父事件
# tag_access.set_tag_value(tag_thin_ev, 0)
# sleep()

sys.exit(0)
