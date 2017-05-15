#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'jhg'

import TagSimulator
import time
import random

time_interval = 5

tag_access = TagSimulator.TagAccess()

# 配置 tagname
tg_GENERAL_EV			= 'GENERAL_EV'
tg_HJ_TEMP_CL_2083		= 'HJ_TEMP_CL_2083'
tg_HJ_HUMI_CL_2083		= 'HJ_HUMI_CL_2083'
tg_HJ_TEMP_CC_2087		= 'HJ_TEMP_CC_2087'
tg_HJ_HUMI_CC_2087		= 'HJ_HUMI_CC_2087'
tg_HJ_TEMP_PY_2081		= 'HJ_TEMP_PY_2081'
tg_HJ_HUMI_PY_2081		= 'HJ_HUMI_PY_2081'
tg_HJ_FL_ENV_TEMP		= 'HJ_FL_ENV_TEMP'
tg_HJ_FL_ENV_HUM		= 'HJ_FL_ENV_HUM'
tg_HJ_STB_ENV_TEMP		= 'HJ_STB_ENV_TEMP'
tg_HJ_STB_ENV_HUM		= 'HJ_STB_ENV_HUM'

def sleep():
    time.sleep(1)

# 设置父信号
tag_access.set_tag_value(tg_GENERAL_EV, 1)
print tg_GENERAL_EV, '=', tag_access.get_tag_value(tg_GENERAL_EV)
sleep()

# �����¶�����
while 1 :
  tag_access.set_tag_value(tg_HJ_TEMP_CL_2083	, random.randint(17, 37))
  tag_access.set_tag_value(tg_HJ_HUMI_CL_2083	, random.randint(43, 65))
  tag_access.set_tag_value(tg_HJ_TEMP_CC_2087	, random.randint(17, 37))
  tag_access.set_tag_value(tg_HJ_HUMI_CC_2087	, random.randint(43, 65))
  tag_access.set_tag_value(tg_HJ_TEMP_PY_2081	, random.randint(17, 37))
  tag_access.set_tag_value(tg_HJ_HUMI_PY_2081	, random.randint(43, 65))

  tag_access.set_tag_value(tg_HJ_FL_ENV_TEMP	, random.randint(18, 26))
  tag_access.set_tag_value(tg_HJ_FL_ENV_HUM	, random.randint(45, 65))
  tag_access.set_tag_value(tg_HJ_STB_ENV_TEMP	, random.randint(20, 30))
  tag_access.set_tag_value(tg_HJ_STB_ENV_HUM	, random.randint(46, 56))

  print 'set ', tg_HJ_TEMP_CL_2083	, ' = ',  tag_access.get_tag_value(tg_HJ_TEMP_CL_2083	)
  print 'set ', tg_HJ_HUMI_CL_2083	, ' = ',  tag_access.get_tag_value(tg_HJ_HUMI_CL_2083	)
  print 'set ', tg_HJ_TEMP_CC_2087	, ' = ',  tag_access.get_tag_value(tg_HJ_TEMP_CC_2087	)
  print 'set ', tg_HJ_HUMI_CC_2087	, ' = ',  tag_access.get_tag_value(tg_HJ_HUMI_CC_2087	)
  print 'set ', tg_HJ_TEMP_PY_2081	, ' = ',  tag_access.get_tag_value(tg_HJ_TEMP_PY_2081	)
  print 'set ', tg_HJ_HUMI_PY_2081	, ' = ',  tag_access.get_tag_value(tg_HJ_HUMI_PY_2081	)
  print 'set ', tg_HJ_FL_ENV_TEMP	, ' = ',  tag_access.get_tag_value(tg_HJ_FL_ENV_TEMP	)
  print 'set ', tg_HJ_FL_ENV_HUM	, ' = ',  tag_access.get_tag_value(tg_HJ_FL_ENV_HUM		)
  print 'set ', tg_HJ_STB_ENV_TEMP	, ' = ',  tag_access.get_tag_value(tg_HJ_STB_ENV_TEMP	)
  print 'set ', tg_HJ_STB_ENV_HUM	, ' = ',  tag_access.get_tag_value(tg_HJ_STB_ENV_HUM	)

  time.sleep(time_interval)


input('Press enter to continue . . .')

