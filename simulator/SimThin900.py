#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Yefeng'

import TagSimulator
import time
import random

tag_access = TagSimulator.TagAccess()

# 定义 tagname
tagname_thin_ev = 'TK_THIN_EV'
tagname_thin_cip_ev = 'TK_THIN_CIP_EV'
tagname_thin_cip_elec = 'TK_THIN_CIP_ELEC'
tagname_thin_sip_ev = 'TK_THIN_SIP_EV'
tagname_thin_sip_temp = 'TK_THIN_SIP_TEMP'
tagname_thin_tt03_temp = 'TK_THIN_TT03_TEMP'
tagname_thin_tt04_temp = 'TK_THIN_TT04_TEMP'
tagname_thin_tt08_temp = 'TK_THIN_TT08_TEMP'
tagname_thin_tt09_temp = 'TK_THIN_TT09_TEMP'
tagname_thin_sip_pres = 'TK_THIN_SIP_PRES'

# 计算电导率
def cond(t):
    return round(-0.1649 * t + 10, 2)

def sleep():
    time.sleep(1)

# 开始父事件
tag_access.set_tag_value(tagname_thin_ev, 1)
print tagname_thin_ev, '=', tag_access.get_tag_value(tagname_thin_ev)
sleep()

# 开始 cip 事件
tag_access.set_tag_value(tagname_thin_cip_ev, 1)
print tagname_thin_cip_ev, '=', tag_access.get_tag_value(tagname_thin_cip_ev)
sleep()

# 写电导率 tag
for t in range(60):
    tag_access.set_tag_value(tagname_thin_cip_elec, cond(t))
    print tagname_thin_cip_elec, '=', tag_access.get_tag_value(tagname_thin_cip_elec)
    sleep()

# 结束 cip 事件
tag_access.set_tag_value(tagname_thin_cip_ev, 0)
sleep()

# 开始 sip 事件
tag_access.set_tag_value(tagname_thin_sip_ev, 1)
sleep()

random.seed(time.time())

# 写 sip tag
for t in range(60):
    tag_access.set_tag_value(tagname_thin_sip_temp, random.randint(121, 127))
    print tagname_thin_sip_temp, '=', tag_access.get_tag_value(tagname_thin_sip_temp)

    tag_access.set_tag_value(tagname_thin_tt03_temp, random.randint(121, 127))
    print tagname_thin_tt03_temp, '=', tag_access.get_tag_value(tagname_thin_tt03_temp)

    tag_access.set_tag_value(tagname_thin_tt04_temp, random.randint(121, 127))
    print tagname_thin_tt04_temp, '=', tag_access.get_tag_value(tagname_thin_tt04_temp)

    tag_access.set_tag_value(tagname_thin_tt08_temp, random.randint(121, 127))
    print tagname_thin_tt08_temp, '=', tag_access.get_tag_value(tagname_thin_tt08_temp)

    tag_access.set_tag_value(tagname_thin_tt09_temp, random.randint(121, 127))
    print tagname_thin_tt09_temp, '=', tag_access.get_tag_value(tagname_thin_tt09_temp)

    tag_access.set_tag_value(tagname_thin_sip_pres, round(random.uniform(2.1, 2.7), 2))
    print tagname_thin_sip_pres, '=', tag_access.get_tag_value(tagname_thin_sip_pres)

    sleep()

# 结束 sip 事件
tag_access.set_tag_value(tagname_thin_sip_ev, 0)
sleep()

# 结束父事件
tag_access.set_tag_value(tagname_thin_ev, 0)
sleep()

input('Press enter to continue . . .')
