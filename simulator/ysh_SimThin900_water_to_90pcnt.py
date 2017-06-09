#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 稀配罐加水模拟
__author__ = 'phoenix'

import TagSimulator
import time
import random
import sys

tag_access = TagSimulator.TagAccess()

# 定义 tagname
tag_thin_water_ev 		= 'IOS.MESPY3_DI_0016'
tag_thin_weight	 		= 'IOS.MESPY3_AI_0021'


time_interval			= 3
total_seconds			= 8

qty_min					= 480
qty_max					= 540



# 生成数据，
def water(min, max, count, step):
	return min + ( max - min ) / count * step + random.uniform(-0.5,0.5) * 0.2 * ( max - min ) / count

def sleep():
  time.sleep(1)


# 开始 WATER 事件
tag_access.set_tag_value(tag_thin_water_ev, 1)
print tag_thin_water_ev, '=', tag_access.get_tag_value(tag_thin_water_ev)
sleep()
	
# 生成初始数据
tag_access.set_tag_value(tag_thin_weight, qty_min)
print tag_thin_weight, '=', tag_access.get_tag_value(tag_thin_weight)
sleep()

# 生成数据，有随机量， tag
for idx in range(1, total_seconds):
	tag_access.set_tag_value(tag_thin_weight, water(qty_min, qty_max, total_seconds, idx))

	print tag_thin_weight, '=', tag_access.get_tag_value(tag_thin_weight)
	print "==============================华丽丽的分割线=================================="
	sleep()
	
# 生成最终数据
tag_access.set_tag_value(tag_thin_weight, qty_max)
print tag_thin_weight, '=', tag_access.get_tag_value(tag_thin_weight)
sleep()

# 结束 WATER 事件
tag_access.set_tag_value(tag_thin_water_ev, 0)
sleep()

#input('Press enter to continue . . .')

sys.exit(0)
