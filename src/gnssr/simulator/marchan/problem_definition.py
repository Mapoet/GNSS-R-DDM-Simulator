#!/usr/bin/env python

import numpy as np

h_t = 16836198.649 # meters
h_r = 612487.690 # meters
elevation = 45*np.pi/180 # rad

# Coordinate Frame as defined in Figure 2
#      J. F. Marchan-Hernandez, A. Camps, N. Rodriguez-Alvarez, E. Valencia, X. 
#      Bosch-Lluis, and I. Ramos-Perez, “An Efficient Algorithm to the Simulation of 
#      Delay–Doppler Maps of Reflected Global Navigation Satellite System Signals,” 
#      IEEE Transactions on Geoscience and Remote Sensing, vol. 47, no. 8, pp. 
#      2733–2740, Aug. 2009.  
r_t = np.array([0,h_t/np.tan(elevation),h_t])
r_r = np.array([0,-h_r/np.tan(elevation),h_r])

# Velocity
v_t = np.array([-2684.911, 1183.799, -671.829]) # m/s
v_r = np.array([6043.852, -4654.310, -315.129]) # m/s

light_speed = 299792458.0 # m/s

# GPS L1 center frequency is defined in relation to a reference frequency 
# f_0 = 10.23e6, so that f_carrier = 154*f_0 = 1575.42e6 # Hz 
# Explained in section 'DESCRIPTION OF THE EMITTED GPS SIGNAL' in Zarotny 
# and Voronovich 2000
f_0 = 10.23e6 # Hz
f_carrier = 154*f_0

fresnel_coefficient = 1 # TODO

integration_time = 1e-3 # seconds
delay_chip =  1/1.023e6 # seconds
# Wind speed at 10 meters above sea surface
u_10 =  8.0 # m/s 
# Angle between the up-down wind direction and the x-axis
#phi_0 = (135)*np.pi/180 # rad 
phi_0 = (135)*np.pi/180 # rad 

delay_start = -2*delay_chip # seconds
delay_end = 55*delay_chip # seconds
#delay_resolution = 0.3*delay_chip # seconds
delay_resolution = 0.25*delay_chip # seconds

doppler_start = -6000 # Hz
doppler_end = 6000 # Hz
#doppler_start = -2500 # Hz
#doppler_end = -1200 # Hz
doppler_resolution = 40.0 # Hz
