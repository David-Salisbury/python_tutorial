#!/usr/bin/python
# comment


def compute_windchill(t,v):
   """
   Only valid for temperatures between -45F and +45F and windspeeds 3 to 60 mph
   Parameters
   t: temperature
   v:  speed
   """

   a = 35
   b = 0.62
   c = 35
   d = 0.42

   v16 = v ** 0.16

   wci = a + ( b * t ) - ( c * v16) + ( d*t*v16 )
   return wci 



def compute_heatindex(t,hum):
   """
   """
   a = -42.3
   b = 2.04
   c = 10.14
   d = 0.22
   e = 0.006837
   f = 0.054

   rh = 1






