#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'jhg'

import TagSimulator
import time
import random

tag_access = TagSimulator.TagAccess()

# 定义 tagname
tag_GENERAL_EV				= 'GENERAL_EV'

tag_RM_2222_TEMP			= 'EMS0303T4_303'
tag_RM_2222_HUMI        	= 'EMS0303H4_305'
tag_RM_2221_TEMP        	= 'EMS0303T5_303'
tag_RM_2221_HUMI        	= 'EMS0303H5_305'
tag_RM_2229_TEMP        	= 'EMS0303T6_303'
tag_RM_2229_HUMI        	= 'EMS0303H6_305'
tag_RM_2229_PRESS_DIF   	= 'RM_2229_PRESS_DIF'
tag_RM_2209_PRESS_DIF   	= 'RM_2209_PRESS_DIF'
tag_RM_2211_TEMP        	= 'EMS0303T2_303'
tag_RM_2211_HUMI        	= 'EMS0303H2_305'
tag_RM_2211_PRESS_DIF   	= 'RM_2211_PRESS_DIF'
tag_RM_2234_TEMP        	= 'EMS0303T3_303'
tag_RM_2234_HUMI        	= 'EMS0303H3_305'
tag_RM_2244_PRESS_DIF   	= 'RM_2244_PRESS_DIF'


time_interval			= 5

def sleep():
    time.sleep(1)

# 开始公共信号
tag_access.set_tag_value(tag_GENERAL_EV, 1)
print tag_GENERAL_EV, '=', tag_access.get_tag_value(tag_GENERAL_EV)
sleep()

# 设置温度数据
while 1 :
  tag_access.set_tag_value(tag_RM_2222_TEMP			, random.randint(17, 37))
  tag_access.set_tag_value(tag_RM_2222_HUMI        	, random.randint(43, 65))
  tag_access.set_tag_value(tag_RM_2221_TEMP        	, random.randint(17, 37))
  tag_access.set_tag_value(tag_RM_2221_HUMI        	, random.randint(43, 65))
  tag_access.set_tag_value(tag_RM_2229_TEMP        	, random.randint(17, 37))
  tag_access.set_tag_value(tag_RM_2229_HUMI        	, random.randint(43, 65))
  tag_access.set_tag_value(tag_RM_2229_PRESS_DIF   	, random.randint(10,15))
  tag_access.set_tag_value(tag_RM_2209_PRESS_DIF   	, random.randint(10,15))
  tag_access.set_tag_value(tag_RM_2211_TEMP        	, random.randint(17, 37))
  tag_access.set_tag_value(tag_RM_2211_HUMI        	, random.randint(43, 65))
  tag_access.set_tag_value(tag_RM_2211_PRESS_DIF   	, random.randint(10,15))
  tag_access.set_tag_value(tag_RM_2234_TEMP        	, random.randint(17, 37))
  tag_access.set_tag_value(tag_RM_2234_HUMI        	, random.randint(43, 65))
  tag_access.set_tag_value(tag_RM_2244_PRESS_DIF   	, random.randint(10,15))

  print 'set ', tag_RM_2222_TEMP			, ' = ',  tag_access.get_tag_value(tag_RM_2222_TEMP			)
  print 'set ', tag_RM_2222_HUMI        	, ' = ',  tag_access.get_tag_value(tag_RM_2222_HUMI     	)
  print 'set ', tag_RM_2221_TEMP        	, ' = ',  tag_access.get_tag_value(tag_RM_2221_TEMP     	)
  print 'set ', tag_RM_2221_HUMI        	, ' = ',  tag_access.get_tag_value(tag_RM_2221_HUMI     	)
  print 'set ', tag_RM_2229_TEMP        	, ' = ',  tag_access.get_tag_value(tag_RM_2229_TEMP     	)
  print 'set ', tag_RM_2229_HUMI        	, ' = ',  tag_access.get_tag_value(tag_RM_2229_HUMI     	)
  print 'set ', tag_RM_2229_PRESS_DIF   	, ' = ',  tag_access.get_tag_value(tag_RM_2229_PRESS_DIF	)
  print 'set ', tag_RM_2209_PRESS_DIF   	, ' = ',  tag_access.get_tag_value(tag_RM_2209_PRESS_DIF	)
  print 'set ', tag_RM_2211_TEMP        	, ' = ',  tag_access.get_tag_value(tag_RM_2211_TEMP     	)
  print 'set ', tag_RM_2211_HUMI        	, ' = ',  tag_access.get_tag_value(tag_RM_2211_HUMI     	)
  print 'set ', tag_RM_2211_PRESS_DIF   	, ' = ',  tag_access.get_tag_value(tag_RM_2211_PRESS_DIF	)
  print 'set ', tag_RM_2234_TEMP        	, ' = ',  tag_access.get_tag_value(tag_RM_2234_TEMP     	)
  print 'set ', tag_RM_2234_HUMI        	, ' = ',  tag_access.get_tag_value(tag_RM_2234_HUMI     	)
  print 'set ', tag_RM_2244_PRESS_DIF   	, ' = ',  tag_access.get_tag_value(tag_RM_2244_PRESS_DIF	)


  print '-----------------------------华丽丽的分割线-----------------------------'
  time.sleep(time_interval)


input('Press enter to continue . . .')

