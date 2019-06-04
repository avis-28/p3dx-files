#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

topic_cmd_vel ='/p3dx/cmd_vel'
update_interval = 0.1

vel_lin = input("enter the velocity")
radius = input("enter the radius of te circle")
vel_ang = vel_lin/radius

rospy.init_node('circle')

pub = rospy.Publisher(topic_cmd_vel, Twist,queue_size=10)

while not rospy.is_shutdown():

   pub.publish(Twist(Vector3(vel_lin, 0, 0), Vector3(0, 0, vel_ang)))

   rospy.sleep(update_interval)
