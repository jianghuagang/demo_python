import numpy
import pyfits
import os
import datetime
import time
from array import array

int_number_scan = 30
int_size_spectrum = 1000
string_format_spectrum = '1000E'

float_obstime = numpy.zeros((int_number_scan,),dtype=numpy.float32)
float_spectrum = numpy.zeros((int_number_scan,int_size_spectrum),dtype=numpy.float32)


for i in xrange(int_number_scan):
  float_obstime[i] = time.mktime(time.gmtime())
  float_spectrum[i,:] = numpy.random.random(int_size_spectrum)
  time.sleep(1)
  print i,time.mktime(time.gmtime()),time.mktime(time.localtime())

column1 = pyfits.Column(name='time',format='E',array=float_obstime)
column2 = pyfits.Column(name='spectrum',format=string_format_spectrum,array=float_spectrum)

table_hdu = pyfits.new_table([column1,column2])

phdu = pyfits.PrimaryHDU()

hdulist = pyfits.HDUList([phdu,table_hdu])

if( os.path.isfile('simuobserve.fits')):
  os.remove('simuobserve.fits')

hdulist.writeto('simuobserve.fits')
