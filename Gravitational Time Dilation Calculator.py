import math

def gravitational_time_dilation(velocity):
  # gravitational time dilation formula: t_observer = t_source / sqrt(1 - (v/c)^2)
  # where t_observer is the time observed by an observer, t_source is the time measured by a clock at the source of the gravitational field, v is the velocity of the object, and c is the speed of light
  c = 299792458 # speed of light in m/s
  t_observer = 1 / math.sqrt(1 - (velocity/c)**2)
  return t_observer

# ask the user for an input velocity
velocity = float(input("Enter the velocity of the object in m/s: "))

# calculate and print the gravitational time dilation
time_dilation = gravitational_time_dilation(velocity)
print("The gravitational time dilation is:", time_dilation)
