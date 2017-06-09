#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'phoenix'
# 浓配罐CIP/SIP记录

import TagSimulator
import time
import random
import sys

tag_access = TagSimulator.TagAccess()

# 定义 tagname
tag_dens_cip_ev 	= 'IOS.MESPY3_DI_0039'
tag_dens_cip_elec 	= 'IOS.MESPY3_AI_0004'

tag_dens_sip_ev 	= 'IOS.MESPY3_DI_0065'
tag_dens_sip_temp  	= 'IOS.MESPY3_AI_0011'
tag_dens_sip_pres 	= 'IOS.MESPY3_AI_0015'


tag_dens_sip_drain_temp	= 'IOS.MESPY3_AI_0002'

time_interval			= 1
total_seconds_cip		= 10
total_seconds_sip		= 10


dens_cip_elec_begin		= 10
dens_cip_elec_end		= 0.85

dens_sip_temp_min		= 121
dens_sip_temp_max		= 127

# 计算电导率
def elec(min, max, tot, idx):
	return round( min + ( max - min ) / tot * idx + random.uniform(-0.5, 0.5) * 0.2 * ( max - min ) / tot, 2 )

def sleep():
    time.sleep(1)


# 开始 cip 事件
tag_access.set_tag_value(tag_dens_cip_ev, 1)
print tag_dens_cip_ev, '=', tag_access.get_tag_value(tag_dens_cip_ev)
sleep()

print '---------------------------------------dens cip begins---------------------------------------'
tag_access.set_tag_value(tag_dens_cip_elec, dens_cip_elec_begin)
sleep()

# 写电导率 tag
for idx in range(1, total_seconds_cip):
    tag_access.set_tag_value(tag_dens_cip_elec, elec(dens_cip_elec_begin, dens_cip_elec_end, total_seconds_cip, idx))
    print tag_dens_cip_elec, '=', tag_access.get_tag_value(tag_dens_cip_elec)
    sleep()

tag_access.set_tag_value(tag_dens_cip_elec, dens_cip_elec_end)
sleep()

# 结束 cip 事件
tag_access.set_tag_value(tag_dens_cip_ev, 0)
sleep()

print '---------------------------------------dens cip ends---------------------------------------'

# 开始 sip 事件
tag_access.set_tag_value(tag_dens_sip_ev, 1)
sleep()

print '---------------------------------------dens sip begins---------------------------------------'
random.seed(time.time())

# 写 sip tag
for t in range(total_seconds_sip):
	tag_access.set_tag_value(tag_dens_sip_temp, random.randint(dens_sip_temp_min, dens_sip_temp_max))
	tag_access.set_tag_value(tag_dens_sip_drain_temp, random.randint(dens_sip_temp_min, dens_sip_temp_max))
	tag_access.set_tag_value(tag_dens_sip_pres, round(random.uniform(2.1, 2.7), 2))

	print tag_dens_sip_temp, '=', tag_access.get_tag_value(tag_dens_sip_temp)
	print tag_dens_sip_drain_temp, '=', tag_access.get_tag_value(tag_dens_sip_drain_temp)
	print tag_dens_sip_pres, '=', tag_access.get_tag_value(tag_dens_sip_pres)

	sleep()
	random.seed(time.time())

# 结束 sip 事件
tag_access.set_tag_value(tag_dens_sip_ev, 0)
sleep()


sys.exit(0)
