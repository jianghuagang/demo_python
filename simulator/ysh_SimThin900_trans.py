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
tag_thin_trans_ev 		= 'IOS.MESPY3_DI_0037'
tag_dens_weight	 		= 'IOS.MESPY3_AI_0020'
tag_thin_weight	 		= 'IOS.MESPY3_AI_0021'
tag_stor_weight	 		= 'IOS.MESPY3_AI_0022'

time_interval			= 1
total_seconds			= 60

qty_min					= 0
qty_max					= 600


# 生成数据，
def water(min, max, count, step):
	return min + ( max - min ) / count * step
def sleep():
	time.sleep(1)

# 开始 transfer 事件
tag_access.set_tag_value(tag_thin_trans_ev, 1)
print "==============================dens trans beings=================================="
print tag_thin_trans_ev, '=', tag_access.get_tag_value(tag_thin_trans_ev)


# 生成初始数据
tag_access.set_tag_value(tag_thin_weight, qty_max)
print tag_thin_weight, '=', tag_access.get_tag_value(tag_thin_weight)
sleep()

tag_access.set_tag_value(tag_stor_weight, qty_min)
print tag_stor_weight, '=', tag_access.get_tag_value(tag_stor_weight)
sleep()	

# 生成数据， tag
for idx in range(1, total_seconds):
	tag_access.set_tag_value(tag_thin_weight, water(qty_min, qty_max, total_seconds, idx))
	tag_access.set_tag_value(tag_stor_weight, water(qty_max, qty_min, total_seconds, idx))

	print tag_thin_weight, '=', tag_access.get_tag_value(tag_thin_weight)
	print tag_stor_weight, '=', tag_access.get_tag_value(tag_stor_weight)
	print "==============================华丽丽的分割线=================================="
	sleep()
	
# 生成最终数据
tag_access.set_tag_value(tag_thin_weight, qty_min)
print tag_thin_weight, '=', tag_access.get_tag_value(tag_thin_weight)
sleep()

tag_access.set_tag_value(tag_stor_weight, qty_max)
print tag_stor_weight, '=', tag_access.get_tag_value(tag_stor_weight)
sleep()




#input('Press enter to continue . . .')

sys.exit(0)