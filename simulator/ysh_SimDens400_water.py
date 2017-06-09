#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'phoenix'

import TagSimulator
import time
import random
import sys

tag_access = TagSimulator.TagAccess()

# 定义 tagname
tag_dens_water_ev 		= 'IOS.MESPY3_DI_0003'
tag_dens_weight	 		= 'IOS.MESPY3_AI_0020'


time_interval			= 3
total_seconds			= 60

qty_min					= 0
qty_max					= 300



# 生成数据，
def water(min, max, count, step):
	return min + ( max - min ) / count * step + random.uniform(-0.5,0.5) * 0.2 * ( max - min ) / count

def sleep():
  time.sleep(1)


# 开始 WATER 事件
tag_access.set_tag_value(tag_dens_water_ev, 1)
print tag_dens_water_ev, '=', tag_access.get_tag_value(tag_dens_water_ev)
sleep()
	
# 生成初始数据
tag_access.set_tag_value(tag_dens_weight, qty_min)
print tag_dens_weight, '=', tag_access.get_tag_value(tag_dens_weight)
sleep()

# 生成数据，有随机量， tag
for idx in range(1, total_seconds):
	tag_access.set_tag_value(tag_dens_weight, water(qty_min, qty_max, total_seconds, idx))

	print tag_dens_weight, '=', tag_access.get_tag_value(tag_dens_weight)
	print "==============================华丽丽的分割线=================================="
	sleep()
	
# 生成最终数据
tag_access.set_tag_value(tag_dens_weight, qty_max)
print tag_dens_weight, '=', tag_access.get_tag_value(tag_dens_weight)
sleep()

# 结束 WATER 事件
tag_access.set_tag_value(tag_dens_water_ev, 0)
sleep()


random.seed(time.time())

# 写 sip tag
#for t in range(60):
#    tag_access.set_tag_value(tag_dens_sip_temp, random.randint(121, 127))
#    print tag_dens_sip_temp, '=', tag_access.get_tag_value(tag_dens_sip_temp)
#
#    #tag_access.set_tag_value(tag_dens_tt03_temp, random.randint(121, 127))
#    #print tag_dens_tt03_temp, '=', tag_access.get_tag_value(tag_dens_tt03_temp)
#
#    #tag_access.set_tag_value(tag_dens_tt08_temp, random.randint(121, 127))
#    #print tag_dens_tt08_temp, '=', tag_access.get_tag_value(tag_dens_tt08_temp)
#
#    #tag_access.set_tag_value(tag_dens_tt11_temp, random.randint(121, 127))
#    #print tag_dens_tt11_temp, '=', tag_access.get_tag_value(tag_dens_tt11_temp)
#
#    tag_access.set_tag_value(tag_dens_sip_pres, round(random.uniform(2.1, 2.7), 2))
#    print tag_dens_sip_pres, '=', tag_access.get_tag_value(tag_dens_sip_pres)
#
#    print '-----------------------------华丽丽的分割线-----------------------------'
#    time.sleep(time_interval)
#
# 结束 sip 事件

# input('Press enter to continue . . .')

sys.exit(0)