#!/usr/bin/python
# comment


def compute_windchill(t,v):
   """
   """
   Oarameters
   t: temperature
   v: 

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
   e = o.006837
   f = 0.054

   rh = 1






