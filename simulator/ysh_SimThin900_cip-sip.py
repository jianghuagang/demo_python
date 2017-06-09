#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'phoenix'
# ϡ���CIP/SIP��¼

import TagSimulator
import time
import random
import sys

tag_access = TagSimulator.TagAccess()

# ���� tagname
tag_thin_cip_ev_begin 		= 'IOS.MESPY3_DI_0053'
tag_thin_cip_ev_end 		= 'IOS.MESPY3_DI_0004'
tag_thin_sip_ev		 		= 'IOS.MESPY3_DI_0068'
	
tag_thin_cip_elec 			= 'IOS.MESPY3_AI_0056'
tag_thin_sip_temp 			= 'IOS.MESPY3_AI_0012'
tag_thin_sip_pres 			= 'IOS.MESPY3_AI_0017'

tag_thin_sip_drain_temp_1 	= 'IOS.MESPY3_AI_0001'
tag_thin_sip_drain_temp_2 	= 'IOS.MESPY3_AI_0003'
tag_thin_sip_drain_temp_3 	= 'IOS.MESPY3_AI_0006'



time_interval			= 1
total_seconds_cip		= 10
total_seconds_sip		= 10


thin_cip_elec_begin		= 10
thin_cip_elec_end		= 0.85

thin_sip_temp_min		= 121
thin_sip_temp_max		= 127




# ����絼��
def elec(min, max, tot, idx):
	return round( min + ( max - min ) / tot * idx + random.uniform(-0.5, 0.5) * 0.2 * ( max - min ) / tot, 2 )

def sleep():
    time.sleep(1)


# ��ʼ cip �¼�
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

# д�絼�� tag
for idx in range(1, total_seconds_cip):
    tag_access.set_tag_value(tag_thin_cip_elec, elec(thin_cip_elec_begin, thin_cip_elec_end, total_seconds_cip, idx))
    print tag_thin_cip_elec, '=', tag_access.get_tag_value(tag_thin_cip_elec)
    sleep()

tag_access.set_tag_value(tag_thin_cip_elec, thin_cip_elec_end)
sleep()

# ���� cip �¼�
tag_access.set_tag_value(tag_thin_cip_ev_end, 1)
sleep()

# cip�źŸ�λ
tag_access.set_tag_value(tag_thin_cip_ev_begin, 0)
sleep()
tag_access.set_tag_value(tag_thin_cip_ev_end, 0)
sleep()

# -----------------------------------------
# ��ʼ sip �¼�
tag_access.set_tag_value(tag_thin_sip_ev, 1)
sleep()

# д sip tag
for t in range(total_seconds_sip):
	tag_access.set_tag_value(tag_thin_sip_temp, random.randint(thin_sip_temp_min, thin_sip_temp_max))
	tag_access.set_tag_value(tag_thin_sip_drain_temp_1, random.randint(thin_sip_temp_min, thin_sip_temp_max))
	tag_access.set_tag_value(tag_thin_sip_drain_temp_2, random.randint(thin_sip_temp_min, thin_sip_temp_max))
	tag_access.set_tag_value(tag_thin_sip_drain_temp_3, random.randint(thin_sip_temp_min, thin_sip_temp_max))
	tag_access.set_tag_value(tag_thin_sip_pres, round(random.uniform(2.1, 2.7), 2))

	print '-----------------------------�������ķָ���-----------------------------'
	print tag_thin_sip_temp, '=', tag_access.get_tag_value(tag_thin_sip_temp)
	print tag_thin_sip_drain_temp_1, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_1)
	print tag_thin_sip_drain_temp_2, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_2)
	print tag_thin_sip_drain_temp_3, '=', tag_access.get_tag_value(tag_thin_sip_drain_temp_3)
	print tag_thin_sip_pres, '=', tag_access.get_tag_value(tag_thin_sip_pres)

	sleep()
	random.seed(time.time())

# ���� sip �¼�
tag_access.set_tag_value(tag_thin_sip_ev, 0)
sleep()

# �������¼�
# tag_access.set_tag_value(tag_thin_ev, 0)
# sleep()

sys.exit(0)
