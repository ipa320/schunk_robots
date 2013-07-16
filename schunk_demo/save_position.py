#!/usr/bin/env python

#################################################################
##\file
#
# \note
# Copyright (c) 2013 \n
# Fraunhofer Institute for Manufacturing Engineering
# and Automation (IPA) \n\n
#
#################################################################
#
# \note
# Project name: Care-O-bot Research
# \note
# ROS package name: 
#
# \author
# Author: Thiago de Freitas Oliveira Araujo, 
# email:thiago.de.freitas.oliveira.araujo@ipa.fhg.de
# \author
# Supervised by: Florian Weisshardt, email:florian.weisshardt@ipa.fhg.de
#
# \date Date of creation: April 2013
#
# \brief
# Saves current arm position
#
#################################################################
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# - Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer. \n
# - Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution. \n
# - Neither the name of the Fraunhofer Institute for Manufacturing
# Engineering and Automation (IPA) nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission. \n
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License LGPL as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License LGPL for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License LGPL along with this program.
# If not, see < http://www.gnu.org/licenses/>.
#
#################################################################

import roslib;
roslib.load_manifest("schunk_demo")
import rospy
import rosparam
import getopt
import sys
from sys import *
from control_msgs.msg import *
from simple_script_server import *

from pr2_controllers_msgs.msg import *

class save_pose:
    
    def __init__(self):
       
        self.sss = simple_script_server()
        self.pose = ''
        self.joint_state = []
        
        
        
        try:
            opts, args = getopt.getopt(sys.argv[1:],"h:p:",["pose="])
            rospy.loginfo(args)
        except getopt.GetoptError:
            print 'python save_position.py -p <posename>'
            sys.exit(2)
        for opt, arg in opts:   
            if opt == '-h':
                print 'python save_position.py -p <posename>'
                sys.exit()
            elif opt in ("-p", "--pose"):
                self.pose = arg
            else:
                print 'Invalid syntax, please use "python save_position.py -p <posename>"'
        
        rospy.loginfo(self.pose)

        if self.pose == '':
            rospy.logerr("posename cannot be empty")
            print 'python save_position.py -p <posename>'
            sys.exit()
        
        rospy.loginfo(self.pose)
        
        self.param = '/script_server/arm/' + self.pose
        
        rospy.loginfo(self.param)
        
        self.ready = 0
        
        rospy.Subscriber('/arm_controller/state', JointTrajectoryControllerState, self.get_joint_state)
        
    def get_joint_state(self, msg):
        self.joint_state = list(msg.actual.positions)
        self.ready = 1
        
    def check_ss(self):
    
        pose_exists = rospy.has_param(self.param)
        
        if(pose_exists):
            c_pose = rospy.get_param(self.param)
            rospy.loginfo("Pose Exists")
            self.update_params()
            
    def update_params(self):
        rospy.loginfo(self.joint_state)
        jl = []
        jl.append(self.joint_state)
        rospy.set_param(self.param, jl)
            
if __name__=="__main__":
    rospy.init_node("save_pose")
    sp = save_pose()
    
    r = rospy.Rate(10)
    
    while(not sp.ready):
        r.sleep()
        
    sp.check_ss()
