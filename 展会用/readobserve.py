import numpy 
import pyfits
import os

if( os.path.isfile('simuobserve.fits') ):
  hdulist = pyfits.open('simuobserve.fits')
  hdu0 = hdulist[0]
  hdu1 = hdulist[1]
  data = hdu1.data
  spec = data.field(1)
  print spec[0,:]
else:
  print "File dose not exit!"
