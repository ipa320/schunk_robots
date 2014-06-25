#!/usr/bin/env python
#fixed can't read /var/mail/

import rospy
import brics_actuator.msg
import math 

def velPub():
  pub = rospy.Publisher("/arm_controller/command_vel",brics_actuator.msg.JointVelocities,queue_size=10)
  rospy.init_node("velPub",anonymous=True)
  r = rospy.Rate(100)
  ini_time=rospy.get_time()
  vel=brics_actuator.msg.JointVelocities()
  current_time=rospy.get_time()-ini_time
  
  for x in range (0,7):
    dummy_joint_value=brics_actuator.msg.JointValue()
    vel.velocities.append(dummy_joint_value)
  
  while not rospy.is_shutdown():
    #vel.velocities[1].value=math.sin(current_time/3)/20    
    pub.publish(vel)
    print("En esta hay %s" % vel.velocities[1])
    print("Tiempo: %s"%current_time)
    r.sleep()

if __name__ == '__main__':
  try:
      velPub()
  except rospy.ROSInterruptException: pass
