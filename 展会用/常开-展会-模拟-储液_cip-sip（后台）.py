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
tag_stor_cip_ev 	= 'IOS.MESPY3_DI_0059'
tag_stor_cip_elec 	= 'IOS.MESPY3_AI_0004'

tag_stor_sip_ev 	= 'IOS.MESPY3_DI_0071'
tag_stor_sip_temp  	= 'IOS.MESPY3_AI_0011'
tag_stor_sip_drain_temp	= 'IOS.MESPY3_AI_0007'

tag_stor_sip_pres 	= 'IOS.MESPY3_AI_0013'



time_interval			= 1
total_seconds_cip		= 60
total_seconds_sip		= 60
total_seconds_ideal		= 30


stor_cip_elec_begin		= 9.8
stor_cip_elec_end		= 0.23

stor_sip_temp_min		= 121
stor_sip_temp_max		= 127

stor_room_temp_min		= 20
stor_room_temp_max		= 27

total_seconds_sip_normal	= 60
total_seconds_sip_heating	= 60
total_seconds_sip_cooling	= 60

# 计算电导率
def elec(min, max, tot, idx):
	return round( min + ( max - min ) / tot * idx + random.uniform(-0.5, 0.5) * 0.2 * ( max - min ) / tot, 2 )
	
# 模拟降温，模拟升温
def simu_line(val1, val2, tot, idx):
	random.seed(time.time())
	return val1 + ( val2 - val1 ) / tot * ( idx - random.uniform(-0.5, 0.5) * 0.59 )


# 模拟常温
def simu_random(val1, val2):
	random.uniform(val1, val2)

def sleep():
    time.sleep(1)


while 1:
	# 开始cip 事件
	tag_access.set_tag_value(tag_stor_cip_ev, 1)
	sleep()
	print '---------------------------------------stor cip begins---------------------------------------'
	print tag_stor_cip_ev, '=', tag_access.get_tag_value(tag_stor_cip_ev)
	print '-------------------------'

	print '-----------------------------stor cip begins-----------------------------'
	tag_access.set_tag_value(tag_stor_cip_elec, stor_cip_elec_begin)
	print tag_stor_cip_elec, '=', tag_access.get_tag_value(tag_stor_cip_elec)
	sleep()

	# 写电导率 tag
	for idx in range(1, total_seconds_cip):
		tag_access.set_tag_value(tag_stor_cip_elec, elec(stor_cip_elec_begin, stor_cip_elec_end, total_seconds_cip, idx))
		print tag_stor_cip_elec, '=', tag_access.get_tag_value(tag_stor_cip_elec)
		sleep()

	tag_access.set_tag_value(tag_stor_cip_elec, stor_cip_elec_end)
	print tag_stor_cip_elec, '=', tag_access.get_tag_value(tag_stor_cip_elec)
	sleep()

	# 结束 cip 事件
	tag_access.set_tag_value(tag_stor_cip_ev, 0)
	sleep()

	print '---------------------------------------stor cip ends---------------------------------------'
	print tag_stor_cip_ev, '=', tag_access.get_tag_value(tag_stor_cip_ev)
	print '-------------------------'
	
	print '-------------------------------sip normal-------------------------------'
	# 常温区
	for t in range(total_seconds_sip_normal):
		tag_access.set_tag_value(tag_stor_sip_temp, random.randint(stor_room_temp_min - 2, stor_room_temp_max + 1))
		random.seed(time.time())
		tag_access.set_tag_value(tag_stor_sip_drain_temp, random.randint(stor_room_temp_min + 1, stor_room_temp_max - 1))
		tag_access.set_tag_value(tag_stor_sip_pres, round(random.uniform(0.5, 0.75), 2))

		print tag_stor_sip_temp, '=', tag_access.get_tag_value(tag_stor_sip_temp)
		print tag_stor_sip_drain_temp, '=', tag_access.get_tag_value(tag_stor_sip_drain_temp)
		print tag_stor_sip_pres, '=', tag_access.get_tag_value(tag_stor_sip_pres)

		sleep()
		random.seed(time.time())



	print '-------------------------------sip heating-------------------------------'
	# 升温区
	for t in range(total_seconds_sip_heating):
		tag_access.set_tag_value(tag_stor_sip_temp, 		round(simu_line(stor_room_temp_max - 2, stor_sip_temp_min + 2, total_seconds_sip_heating, t), 1 ) )
		random.seed(time.time())
		tag_access.set_tag_value(tag_stor_sip_drain_temp, 	round(simu_line(stor_room_temp_max + 2, stor_sip_temp_min - 2, total_seconds_sip_heating, t), 1 ) )
		tag_access.set_tag_value(tag_stor_sip_pres, round(simu_line(0.75, 1.98, total_seconds_sip_heating, t), 2))

		print tag_stor_sip_temp, '=', tag_access.get_tag_value(tag_stor_sip_temp)
		print tag_stor_sip_drain_temp, '=', tag_access.get_tag_value(tag_stor_sip_drain_temp)
		print tag_stor_sip_pres, '=', tag_access.get_tag_value(tag_stor_sip_pres)

		sleep()
		random.seed(time.time())
	

	# 开始sip 事件
	tag_access.set_tag_value(tag_stor_sip_ev, 1)
	sleep()
	
	print '---------------------------------------stor sip begins---------------------------------------'
	print tag_stor_sip_ev, '=', tag_access.get_tag_value(tag_stor_sip_ev)
	print '-------------------------'

	# sip tag
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
	
	print '---------------------------------------stor sip ends---------------------------------------'
	print tag_stor_sip_ev, '=', tag_access.get_tag_value(tag_stor_sip_ev)
	print '-------------------------'

	print '-------------------------------sip cooling-------------------------------'
	# 降温区
	for t in range(total_seconds_sip_cooling):
		tag_access.set_tag_value(tag_stor_sip_temp, round(simu_line(stor_sip_temp_max + 2, stor_room_temp_max + 2, total_seconds_sip_cooling, t), 0 ) )
		random.seed(time.time())
		tag_access.set_tag_value(tag_stor_sip_drain_temp, round(simu_line(stor_sip_temp_max - 2, stor_room_temp_max - 2, total_seconds_sip_cooling, t), 0 ) )
		tag_access.set_tag_value(tag_stor_sip_pres, round(simu_line(1.98, 0.75, total_seconds_sip_cooling, t), 2))

		print tag_stor_sip_temp, '=', tag_access.get_tag_value(tag_stor_sip_temp)
		print tag_stor_sip_drain_temp, '=', tag_access.get_tag_value(tag_stor_sip_drain_temp)
		print tag_stor_sip_pres, '=', tag_access.get_tag_value(tag_stor_sip_pres)

		sleep()
		random.seed(time.time())


	# ideal time 
	time.sleep(total_seconds_ideal)


sys.exit(0)
