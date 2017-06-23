#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ��ʼת���ź�
__author__ = 'phoenix'

import TagSimulator
import time
import random
import sys
import msvcrt

tag_access = TagSimulator.TagAccess()

# ���� tagname
tag_dens_trans_ev 		= 'IOS.MESPY3_DI_0004'
tag_dens_weight	 		= 'IOS.MESPY3_AI_0020'
tag_thin_weight	 		= 'IOS.MESPY3_AI_0021'

time_interval			= 1
total_seconds			= 10

qty_min					= 0
qty_max					= 300


# �������ݣ�
def water(min, max, count, step):
	return min + ( max - min ) / count * step
def sleep():
	time.sleep(1)


# ��ʼ transfer �¼�
tag_access.set_tag_value(tag_dens_trans_ev, 1)
print "==============================dens trans beings=================================="
print tag_dens_trans_ev, '=', tag_access.get_tag_value(tag_dens_trans_ev)

#time.sleep(total_seconds + random.randint(1,8))

# ���ɳ�ʼ����
tag_access.set_tag_value(tag_dens_weight, qty_max)
print tag_dens_weight, '=', tag_access.get_tag_value(tag_dens_weight)
sleep()

tag_access.set_tag_value(tag_thin_weight, qty_min)
print tag_thin_weight, '=', tag_access.get_tag_value(tag_thin_weight)
sleep()

# �������ݣ� tag
for idx in range(1, total_seconds):
	tag_access.set_tag_value(tag_dens_weight, water(qty_min, qty_max, total_seconds, idx))
	tag_access.set_tag_value(tag_thin_weight, water(qty_max, qty_min, total_seconds, idx))

	print tag_dens_weight, '=', tag_access.get_tag_value(tag_dens_weight)
	print tag_thin_weight, '=', tag_access.get_tag_value(tag_thin_weight)
	print "==============================�������ķָ���=================================="
	sleep()
	
# ������������
tag_access.set_tag_value(tag_dens_weight, qty_min)
print tag_dens_weight, '=', tag_access.get_tag_value(tag_dens_weight)
sleep()

tag_access.set_tag_value(tag_thin_weight, qty_max)
print tag_thin_weight, '=', tag_access.get_tag_value(tag_thin_weight)
sleep()


# ���� transfer �¼�
tag_access.set_tag_value(tag_dens_trans_ev, 0)
print "==============================dens trans ends=================================="
print tag_dens_trans_ev, '=', tag_access.get_tag_value(tag_dens_trans_ev)

#input('Press enter to continue . . .')

sys.exit(0)
